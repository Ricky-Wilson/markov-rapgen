#Compatible with Python 3.6+
import sys
import os
import pickle
import markovify
from settings import available_texts
from settings import DB_FILE, FILE_OUT, STATE_SIZE
from settings import MAX_SENTENCES, MAX_SENTENCE_LEN


#Prompts input and returns filepaths, weights
def prompt_input():

    #Displays a list of all items in available_texts
    for i, text in enumerate(available_texts):
        print("{} - {}".format(i, text[0]))

    #Prompts input and splits input into list
    #CHecks Python version
    if sys.version_info[0] < 3:
        nums = raw_input("\nPrint Digits (Space Separated): ").split()
    else:
        nums = input("\nPrint Digits (Space Separated): ").split()

    #Filters and sorts list by only valid numerical indexes
    nums = sorted(set([int(i)
                        for i in nums
                        if (i.isdigit() and int(i) < len(available_texts))]))

    #Use the zip function to grab and sort all the data using indexes.
    names, filenames, weights = zip(*[available_texts[i] for i in nums])

    return names, filenames, weights

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
        except errno.EEXIST:
            pass

    #Opening file as 'wb' = 'write binary'
    #Dump model_combo into the binary pickle file.
    with open(DB_FILE, 'wb') as f:
        pickle.dump(model_combo, f)
    print("Markov Database Generated at " + str(DB_FILE) + "\n")

#Writes markov sentences from Pickle object into file.
def generate_phrase(names, DB_FILE, FILE_OUT):

    #Load binary pickle file
    with open(DB_FILE, 'rb') as f:
        markov_database = pickle.load(f)

    #If database directory/file does not exist, create it
    if not os.path.exists(os.path.dirname(FILE_OUT)):
        try:
            os.makedirs(os.path.dirname(FILE_OUT))
        except errno.EEXIST:
            pass

    #Writes i sentences to file
    with open(FILE_OUT, 'a') as f:

        f.write('\n')
        f.write(str("{} - {}-Gram".format(str(names), str(STATE_SIZE))))
        f.write('\n')

        for i in range(MAX_SENTENCES):
            sentence = str(markov_database.make_short_sentence(MAX_SENTENCE_LEN))
            #Checks whether sentence is 'None' or Nonetype before writing.
            if not (sentence == None or sentence =='None'):
                f.write(sentence)
                f.write('\n')
                print (sentence)
        f.close()
        print('\n')


if __name__ == "__main__":

    names, filenames, weights = prompt_input()
    database_init(filenames, weights, DB_FILE)

    generate_phrase(names, DB_FILE, FILE_OUT)
