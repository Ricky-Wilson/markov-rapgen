
#Bool Triggers for main function.
NEW_DB = True
GENERATE = True

#DB and Output filenames
DB_FILE = "db/markov_database.p"
FILE_OUT = "dist/generated_phrases.txt"

#This value dictates the N-Gram size for the Markov Chain.
#Recomended value at 1 or 2
STATE_SIZE = 2

#Max Sentences
MAX_SENTENCES = 20

#Max Sentence Length
MAX_SENTENCE_LEN = 50

#Dict of available texts to create corpus from -
#Structure: {index: [name, filepath, weight]}
available_texts = [
    ['satan',        'corpus/texts/satanbible.txt', .01    ],
    ['bible',        'corpus/texts/bible.txt',   .03        ],
    ['phys2',        'corpus/textbooks/phys2.txt', .02    ],
    ['kanye',        'corpus/rappers/kanye.txt', .03      ],
    ['lilpump',      'corpus/rappers/lilpump.txt', .7   ],
    ['lilyachty',    'corpus/rappers/lilyachty.txt',.6   ],
    ['gleesh',       'corpus/rappers/gleesh.txt', .6   ],
    ['thugger',      'corpus/rappers/youngthug.txt', .5   ],
    ['travis scott', 'corpus/rappers/travisscott.txt', .5   ],
    ['carti',        'corpus/rappers/carti.txt', .6   ],
]
