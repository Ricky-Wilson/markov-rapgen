#markov bot using source text from anton salazar lavey and isaac asimov
#Author: Brenly
#requires mysqldb python library
#requires markovify python library

#This script creates the initial seed and saves it as a mysqldb for future uses

import markovify
import json

f = open ("anton.txt")
text_anton = f.read()
model_anton = markovify.Text(text_anton, state_size=2)

f = open ("phys2.txt")
text_asimov = f.read()
model_asimov = markovify.Text(text_asimov, state_size=2)


model_combo = markovify.combine([model_asimov, model_anton], [1, 1.4])
#combines two models to generate sentences weighted accordingly 1 to 1.4 created in my opinion the best balance of language

json_model_combo = model_combo.to_json()

with open ('json_main_database.txt', 'w') as outfile:
	json.dump(json_model_combo, outfile)
#with the json database successfully built it can then be reloaded as needed into other scripts