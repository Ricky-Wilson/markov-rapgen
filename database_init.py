#Author: Brenly (& Sharad)
#requires pickle library
#requires markovify github library by @jsvine

import markovify
import pickle
import os


def database_init(input_filenames, weights, DB_FILE):

    model_list = []

    #Loop through input_filenames list and markovify each. Add models to a list
    for filename in input_filenames:
        f = open (filename)
        text = f.read()
        model = markovify.Text(text, state_size=2)
        model_list.append(model)

    #runs the 'combine' function on the model_list and weight listself.
    model_combo = markovify.combine((model_list), weights)

    #Creates the database directory/file if does not exist
    if not os.path.exists(os.path.dirname(DB_FILE)):
        try:
            os.makedirs(os.path.dirname(DB_FILE))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Opening file as 'wb' = 'write binary' because the output file needs to be opened in binary mode.
    #Dumping model_combo into pickle file.
    with open(DB_FILE, 'wb') as f:
        pickle.dump(model_combo, f)
    print("Markov Database Generated at " + str(DB_FILE) + "\n")
