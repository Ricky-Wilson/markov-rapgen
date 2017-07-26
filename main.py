#Compatible with Python 3.6+

from database_init import database_init
from phrase_generator import generate_phrase

NEW_DB = True
GENERATE = True
DB_FILE = "db/markov_database.p"
FILE_OUT = "dist/generated_phrases.txt"

available_texts = {
    0: ['satan',        'corpus/texts/satanbible.txt', .025    ],
    1: ['bible',        'corpus/texts/bible.txt',   .025        ],
    2: ['phys2',        'corpus/textbooks/phys2.txt', .005    ],
    3: ['kanye',        'corpus/rappers/kanye.txt', .03      ],
    4: ['lilpump',      'corpus/rappers/lilpump.txt', .6   ],
    5: ['lilyachty',    'corpus/rappers/lilyachty.txt',.5   ],
}

def prompt_input():
    #Displays a list of all available texts to use
    for key in available_texts.keys():
        print ( str(key) + " - " + str(available_texts[key][0]) )

    #Prompts for input and splits into list
    nums = input("\nPrint Digits (Space Separated): ").split()

    #Adds only valid indexes into list 'nums', and sorts list
    nums = sorted(set([int(i)
                    for i in nums
                    if (i.isdigit() and int(i) < len(available_texts))]))

    #Grabs the directories of the indexes listed in nums
    input_filenames = [ str(available_texts[i][1])
                        for i in nums
                        if (i in available_texts.keys() )]

    #Grabs the weights for the indexes listed in nums
    weights = [ available_texts[i][2]
                for i in nums
                if (i in available_texts.keys() )]

    return input_filenames, weights


if __name__ == "__main__":

    if NEW_DB:
        input_filenames, weights = prompt_input()
        database_init(input_filenames, weights, DB_FILE)

    if GENERATE:
        generate_phrase(DB_FILE, FILE_OUT)
