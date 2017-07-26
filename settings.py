
#Bool Triggers for main function.
NEW_DB = True
GENERATE = True

#DB and Output filenames
DB_FILE = "db/markov_database.p"
FILE_OUT = "dist/generated_phrases.txt"

#This value dictates the text-state size for the Markov Chain.
#Max Recommended = 2
STATE_SIZE = 1

#Max Sentences
MAX_SENTENCES = 10

#Max Sentence Length
MAX_SENTENCE_LEN = 60

#Dict of available texts to create corpus from -
#Structure: {index: [name, filepath, weight]}
available_texts = {
    0: ['satan',        'corpus/texts/satanbible.txt', .01    ],
    1: ['bible',        'corpus/texts/bible.txt',   .03        ],
    2: ['phys2',        'corpus/textbooks/phys2.txt', .02    ],
    3: ['kanye',        'corpus/rappers/kanye.txt', .03      ],
    4: ['lilpump',      'corpus/rappers/lilpump.txt', .4   ],
    5: ['lilyachty',    'corpus/rappers/lilyachty.txt',.6   ],
    6: ['gleesh',       'corpus/rappers/gleesh.txt', .6   ],
    7: ['thugger',      'corpus/rappers/youngthug.txt', .5   ],

}
