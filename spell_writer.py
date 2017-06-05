#markov bot using source text from anton salazar lavey and isaac asimov
#requires markovify from github

import markovify
import json

f = open ("anton.txt")
text_anton = f.read()
model_anton = markovify.Text(text_anton, state_size=2)

f = open ("phys2.txt")
text_asimov = f.read()
model_asimov = markovify.Text(text_asimov, state_size=2)


model_combo = markovify.combine([model_asimov, model_anton], [1, 1.4])
#combines 

#json_model_combo = model_combo.to_json()


#model_combo = markovify.Text.from_json(json_model_combo)
print "\n"
print (model_combo.make_sentence(tries = 50))
print "\n"	
#will try 50 times. the default of 5 tries per generation creates invalid results that do not always pass the final check
