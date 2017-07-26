from database_init import database_init
from phrase_generator import generate_phrase

NEW_DB = True
GENERATE = True
DB_FILE = "db/markov_database.p"
FILE_OUT = "dist/generated_phrases.txt"

available_texts = {
    0: {'satan': 'corpus/texts/satanbible.txt'},
    1: {'bible': 'corpus/texts/bible.txt'},
    2: {'phys2': 'corpus/textbooks/phys2.txt'},
    3: {'kanye': 'corpus/rappers/kanye.txt'},
    4: {'lilpump': 'corpus/rappers/lilpump.txt'},
}

def prompt_input():
    #Displays a list of all available texts to use
    for key in available_texts.keys():
        print (str(key) + " - " + str(available_texts[key].keys()).strip("[]"))
    #Prompts for input and splits into list
    nums = raw_input("\nPrint Digits (Space Separated): ").split()
    #Adds only valid indexes into list, and sorts list
    nums = sorted([int(i)
                    for i in nums
                    if (i.isdigit() and int(i) < len(available_texts))])
    #Grabs the directories of the indexes listed
    input_filenames = [str(available_texts[i].values()).strip("[]").strip("''")
                        for i in nums
                        if i in available_texts.keys() ]
    return input_filenames


if __name__ == "__main__":

    if NEW_DB:
        input_filenames = prompt_input()
        database_init(input_filenames, DB_FILE)

    if GENERATE:
        generate_phrase(DB_FILE, FILE_OUT)
