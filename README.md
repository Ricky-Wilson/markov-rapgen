

# Rapgen

Markov-Chain Rap Lyrics Generator

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
The main file. Run this script in your shell.
Make sure the following parameters are set to True.

```python
NEW_DB = True
GENERATE = True
```

You can set either variable to `False` if you would like to test an individual component.

#### `database_init.py`
This will generate a new database when called.
The database is actually a pickled object stored at `DB_FILE`.


#### `phrase_generator.py`
Generates a new phrase.
Retrieves the pickle object and prints markov sentences.
Set the parameters for sentences here.

#### `corpus/`
Contains all text.

#### `py/`
Unnecessary at the moment.
