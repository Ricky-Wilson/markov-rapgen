#This script does not need to be run!
#it is here for keeping track of project history only!
#pickle database is already built as markov_database.p
#the main section of code will pull phrases from phrases_generated.txt
#running this script will likely result in errors!

#markov database builder using source text from anton salazar lavey and isaac asimov
#Author: Brenly
#requires pickle library
#requires markovify github library by @jsvine

import markovify
import pickle

f = open ("anton.txt")
text_anton = f.read()
model_anton = markovify.Text(text_anton, state_size=2)

f = open ("phys2.txt")
text_asimov = f.read()
model_asimov = markovify.Text(text_asimov, state_size=2)


model_combo = markovify.combine([model_anton, model_asimov], [1.4, 1])
#combines two models to generate sentences weighted accordingly 1 to 1.4 created in my opinion the best balance of language

#this next line is ultimately a bit useless as the next script will generate a txt file of sentences
pickle.dump (model_combo, open("markov_database.p", "w"))

##### this next code segment does not work.
##### there is poor documentation of converting the markov libraries to JSON format so I opted for pickle and plain text file generation
#json_model_combo = model_combo.to_json()
#with open ('main_database.json', 'w') as outfile:
#	json.dump(json_model_combo, outfile)
#with the json database successfully built it can then be reloaded as needed into other scripts