#this script is designed to generate phrases from previous existing databases
#designed to work with the script in the same repository

import markovify
import pickle
import os

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




#code later will pull random lines from phrases_generated.txt instead of metabolizing markov libraries for each message sent
