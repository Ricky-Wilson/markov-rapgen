#this script is designed to generate phrases from previous existing databases
#designed to work with the script in the same repository

import markovify
import pickle
#import json

#with open ('main_database.json', 'r') as json_database:
#	markov_database = json.load(json_database)
#	markov_database = markovify.Text(markov_database)

markov_database = pickle.load(open("markov_database.p", "r"))

for i in range(5):
	print(markov_database.make_sentence())