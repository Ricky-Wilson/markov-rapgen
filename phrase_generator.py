#this script is designed to generate phrases from previous existing databases
#designed to work with the script in the same repository
import markovify
import pickle
import os
#this code does not work
#import json
#will be fixed possibly in future implementations
#with open ('main_database.json', 'r') as json_database:
#	markov_database = json.load(json_database)
#	markov_database = markovify.Text(markov_database)


#pickle library is unecessary in a full implementation but is being included to demonstrate my knowledge
def generate_phrase(DB_FILE, FILE_OUT):
    markov_database = pickle.load(open(DB_FILE, "r"))

    if not os.path.exists(os.path.dirname(FILE_OUT)):
        try:
            os.makedirs(os.path.dirname(FILE_OUT))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(FILE_OUT, 'w') as f:
        for i in range(20):
            sentence = str(markov_database.make_short_sentence(80))
            if not (sentence == None or sentence =='None'):
                f.write(sentence)
                f.write('\n')
                print (sentence)

        f.close()



####
#   for i in range(300):
#	text_file.write(markov_database.make_short_sentence(800))
#	text_file.write ("\n")
	#print(markov_database.make_sentence())

#text_file.close()

#code later will pull random lines from phrases_generated.txt instead of metabolizing markov libraries for each message sent
