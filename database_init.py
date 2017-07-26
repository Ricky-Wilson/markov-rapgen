#This script does not need to be run!
#it is here for keeping track of project history only!
#pickle database is already built as markov_database.p
#the main section of code will pull phrases from phrases_generated.txt
#running this script will likely result in errors!

#markov database builder using source text from isaac asimov
#Author: Brenly
#requires pickle library
#requires markovify github library by @jsvine

import markovify
import pickle


def database_init(input_filenames, DB_FILE):
    print(input_filenames)
    model_list = []

    for filename in input_filenames:
        f = open (filename)
        text = f.read()
        model = markovify.Text(text, state_size=2)
        model_list.append(model)

    #combines two models to generate sentences weighted accordingly 1 to 1.4 created in my opinion the best balance of language
    model_combo = markovify.combine((model_list))

    #this next line is ultimately a bit useless as the next script will generate a txt file of sentences
    #python 3.6 shifted usage of pickle so this will need to be rewritten past 2.7 possibly
    pickle.dump(model_combo, open(DB_FILE, "w"))
    print("Markov Database Generated at " + str(DB_FILE))


##### this next code segment does not work.
##### there is poor documentation of converting the markov libraries to JSON format so I opted for pickle and plain text file generation
#json_model_combo = model_combo.to_json()
#with open ('main_database.json', 'w') as outfile:
#	json.dump(json_model_combo, outfile)
#with the json database successfully built it can then be reloaded as needed into other scripts
