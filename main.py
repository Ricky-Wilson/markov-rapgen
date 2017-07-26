#Compatible with Python 3.6+

import markovify
import pickle
import os

#Bool Triggers for main function.
NEW_DB = True
GENERATE = True

#DB and Output filenames
DB_FILE = "db/markov_database.p"
FILE_OUT = "dist/generated_phrases.txt"

#This value dictates the text-state size for the Markov Chain.
#Max Recommended = 2
STATE_SIZE = 1

#Dict of available texts to create corpus from -
#Structure: {index, [name, filepath, weight]}
available_texts = {
    0: ['satan',        'corpus/texts/satanbible.txt', .01    ],
    1: ['bible',        'corpus/texts/bible.txt',   .003        ],
    2: ['phys2',        'corpus/textbooks/phys2.txt', .005    ],
    3: ['kanye',        'corpus/rappers/kanye.txt', .03      ],
    4: ['lilpump',      'corpus/rappers/lilpump.txt', .6   ],
    5: ['lilyachty',    'corpus/rappers/lilyachty.txt',.6   ],
    6: ['gleesh',       'corpus/rappers/gleesh.txt', .6   ],
}

#Prompts for selections and returns respective filepaths and weights.
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

#Creates Pickle Object using input selections
def database_init(input_filenames, weights, DB_FILE):

    model_list = []

    #Loop through input_filenames list and markovify each. Add models to a list
    for filename in input_filenames:
        f = open (filename)
        text = f.read()
        model = markovify.Text(text, state_size=STATE_SIZE)
        model_list.append(model)

    #runs the 'combine' function on the model_list and weight listself.
    model_combo = markovify.combine((model_list), weights)

    #Creates the database directory/file if does not exist
    if not os.path.exists(os.path.dirname(DB_FILE)):
        try:
            os.makedirs(os.path.dirname(DB_FILE))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Opening file as 'wb' = 'write binary' because the output file needs to be opened in binary mode.
    #Dumping model_combo into pickle file.
    with open(DB_FILE, 'wb') as f:
        pickle.dump(model_combo, f)
    print("Markov Database Generated at " + str(DB_FILE) + "\n")

#Writes phrases from Pickle object into file.
def generate_phrase(DB_FILE, FILE_OUT):

    #Read the Binary pickle file
    with open(DB_FILE, 'rb') as f:
        markov_database = pickle.load(f)

    #Creates the output directory/file if it does not exist
    if not os.path.exists(os.path.dirname(FILE_OUT)):
        try:
            os.makedirs(os.path.dirname(FILE_OUT))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Writes i sentences to file
    with open(FILE_OUT, 'w') as f:
        for i in range(20):
            sentence = str(markov_database.make_short_sentence(80))
            #Checks whether sentence is 'None' or Nonetype before writing.
            if not (sentence == None or sentence =='None'):
                f.write(sentence)
                f.write('\n')
                print (sentence)
        f.close()


if __name__ == "__main__":

    if NEW_DB:
        input_filenames, weights = prompt_input()
        database_init(input_filenames, weights, DB_FILE)

    if GENERATE:
        generate_phrase(DB_FILE, FILE_OUT)
