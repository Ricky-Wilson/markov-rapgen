

# Rapgen

Markov-Chain Rap Lyrics Generator

Future implementations will use a Hidden Markov Model (HMM).

## Setup

You will need Git, Python (v3.6+), and pip to be installed.

**THIS HAS NOT BEEN TESTED ON ANY VERSION BESIDES PYTHON 3.6**

Clone the repo

```
$ git clone https://github.com/sharad-s/markov-rapgen.git
```
Then `cd` into the new folder.

Create a *virtualenv* and activate it:

```
$ virtualenv venv
$ source venv/bin/activate
```

Run `$python --version` to make sure you are running Python 3.x.

If you are not running 3.x:
[install python 3](https://www.python.org/downloads/) and
[create a python3 venv](https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv)

Install dependencies from "requirements.txt" via pip:

```
(venv) $ pip install -r requirements.txt
```

## Execution

Run `main.py`.

```
$ python main.py
```

You will be asked to input digits from a list.
Separate each digit with spaces.

Sentences will be written to the file specified by `FILE_OUT`.
Sentences will also be printed to the screen.


## Structure

#### `main.py`
The main file. Run this script with the command:
```python
python main.py
```

Make sure to have `NEW_DB = True` and `GENERATE = True` in settings for it to run properly.
You can set either variable to `False` if you would like to test an individual component.

#### `settings.py`

Contains all constants and data structures.

`NEW_DB` - (Bool) Controls prompt and db creation.

`GENERATE` - (Bool) Controls text generation.

`DB_FILE` - (String) Specifies Pickle file for read/write.

`FILE_OUT` - (String) Specifies .txt file for write.

`STATE_SIZE` - (Int) Dictates the text-state size for the Markov Chain.

`MAX_SENTENCES` - (Int) Determines # of sentences written.

`MAX_SENTENCE_LEN` - (Int) Sets max length of sentences

`available_texts` - {Dict} Stores all available texts and their details

#### `corpus/`
Contains all text.

#### `py/`
Unnecessary at the moment.
