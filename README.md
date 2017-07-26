


# Rapgen

Markov-Chain Rap Lyrics Generator


## Setup

You will need Git, Python (v2.7), and pip to be installed.

*AS OF NOW, THIS WILL NOT WORK ON ANY VERSION OTHER THAN Python 2.7*

Clone the repo and `cd` into it:

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

Run `main.py`. You will be asked to input digits - separate each digit with spaces.

Sentences will be generated in the file specified by `DB_FILE`
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
