#Compatible with Python 3.6+

import markovify
import pickle
import os
from settings import available_texts
from settings import DB_FILE, FILE_OUT, STATE_SIZE, MAX_SENTENCES
from settings import NEW_DB, GENERATE


#Prompts input and returns filepaths, weights
def prompt_input():

    #Displays a list of all items in available_texts
    for key in available_texts.keys():
        print ( str(key) + " - " + str(available_texts[key][0]) )

    #Prompts input and splits input into list
    nums = input("\nPrint Digits (Space Separated): ").split()

    #Filters and sorts list by only valid numerical indexes
    nums = sorted(set([int(i)
                    for i in nums
                    if (i.isdigit() and int(i) < len(available_texts))]))

    #Grabs the filepaths for the indexes in list
    input_filenames = [ str(available_texts[i][1])
                        for i in nums
                        if (i in available_texts.keys() )]

    #Grabs the weights for the indexes in list
    weights = [ available_texts[i][2]
                for i in nums
                if (i in available_texts.keys() )]

    return input_filenames, weights

#Creates Pickle Object using input selections
def database_init(input_filenames, weights, DB_FILE):

    model_list = []

    #'Markovify' each file from input_filenames. Append to list
    for filename in input_filenames:
        f = open (filename)
        text = f.read()
        model = markovify.Text(text, state_size=STATE_SIZE)
        model_list.append(model)

    model_combo = markovify.combine((model_list), weights)

    #If database directory/file does not exist, create it
    if not os.path.exists(os.path.dirname(DB_FILE)):
        try:
            os.makedirs(os.path.dirname(DB_FILE))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Opening file as 'wb' = 'write binary'
    #Dump model_combo into the binary pickle file.
    with open(DB_FILE, 'wb') as f:
        pickle.dump(model_combo, f)
    print("Markov Database Generated at " + str(DB_FILE) + "\n")

#Writes markov sentences from Pickle object into file.
def generate_phrase(DB_FILE, FILE_OUT):

    #Load binary pickle file
    with open(DB_FILE, 'rb') as f:
        markov_database = pickle.load(f)

    #If database directory/file does not exist, create it
    if not os.path.exists(os.path.dirname(FILE_OUT)):
        try:
            os.makedirs(os.path.dirname(FILE_OUT))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Writes i sentences to file
    with open(FILE_OUT, 'w') as f:
        for i in range(MAX_SENTENCES):
            sentence = str(markov_database.make_short_sentence(80))
            #Checks whether sentence is 'None' or Nonetype before writing.
            if not (sentence == None or sentence =='None'):
                f.write(sentence)
                f.write('\n')
                print (sentence)
        f.close()
        print('\n')


if __name__ == "__main__":

    if NEW_DB:
        input_filenames, weights = prompt_input()
        database_init(input_filenames, weights, DB_FILE)

    if GENERATE:
        generate_phrase(DB_FILE, FILE_OUT)
