#this script is designed to generate phrases from previous existing databases
#designed to work with the script in the same repository
import markovify
import pickle

#this code does not work
#import json
#will be fixed possibly in future implementations
#with open ('main_database.json', 'r') as json_database:
#	markov_database = json.load(json_database)
#	markov_database = markovify.Text(markov_database)


#pickle library is unecessary in a full implementation but is being included to demonstrate my knowledge
def generate_phrase(DB_FILE):
    markov_database = pickle.load(open(DB_FILE, "r"))

    text_file = open("dist/generated_phrases.txt", "w")

    for i in range(20):
        sentence = markov_database.make_short_sentence(80)
        text_file.write(sentence)
        text_file.write('\n')
        print (sentence)

    text_file.close()



####
#   for i in range(300):
#	text_file.write(markov_database.make_short_sentence(800))
#	text_file.write ("\n")
	#print(markov_database.make_sentence())

#text_file.close()

#code later will pull random lines from phrases_generated.txt instead of metabolizing markov libraries for each message sent
