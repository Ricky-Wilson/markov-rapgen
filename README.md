

# Rapgen

Markov-Chain Rap Lyrics Generator

## Setup

You will need Git, Python (v3.6+), and pip to be installed.

**THIS HAS NOT BEEN TESTED ON ANY VERSION BESIDES PYTHON 3.6**

Clone the repo

```
$ git clone https://github.com/sharad-s/markov-rapgen.git
```
`cd` into the new folder:

Create a virtualenv and activate it:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install dependencies from "requirements.txt" via pip:

```
(venv) $ pip install -r requirements.txt
```

## Execution

Run `main.py`.
You will be asked to input digits from a list.
Separate each digit with spaces.

Sentences will be written to the file specified by `DB_FILE`.
Sentences will also be printed to the screen.


## Structure

`database_initializer.py` is a script that uses markovify to build markov text associates between two source texts. it then writes a pickle data to file.

`phrase_generator.py`retrieves the pickle data and prints markov sentences from that pickle data

#### `main.py`
The main file. Run this script in your shell.
Make sure the following parameters are set to True.

```python
NEW_DB = False
GENERATE = False
```

#### `database_init.py`
This will generate a new database when called. Set `NEW_DB = False` to disable this function.

#### `phrase_generator.py`

Generates a new phrase. Set the parameters of this phrase here.
Set `GENERATE = False` to disable this.

#### `corpus/`
Contains all text.

#### `py/`
Unnecessary at the moment.
