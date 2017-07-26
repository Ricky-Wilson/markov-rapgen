This is where I put code to demonstrate python knowledge to any potential employers.

database_initializer.py is a script that uses markovify to build markov text associates between two source texts. it then writes a pickle data to file.
phrase_generator.py retrieves the pickle data and prints 5x markov sentences from that pickle data


# Rapgen

Markov-Chain Rap Lyrics Generator

## Roadmap

- [ ] dev setup
- [ ] data processing
- [ ] continuous pipeline

## Setup

You will need Git, Python (v2.7 or higher), and pip to be installed.

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

## Structure

#### `main.py`

The main file. Run this script in your shell.
Make sure the following parameters are set to True.

```python
NEW_DB = False
GENERATE = False
```


#### `database_init.py`

This will generate a new database when called. Set

```python
NEW_DB = False
```
to disable this function.

#### `phrase_generator.py`

Generates a new phrase. Set the parameters of this phrase here.

#### `corpus/`

Contains all text.

#### `py/`

Unnecessary at the moment.
