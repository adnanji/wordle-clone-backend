# Wordle Clone Backend

---

## Requirements

* Python 3.9.6
* Django 4.0.4
* Colorama 0.4.4
* Django Rest Framework 3.13.1
* Requests 2.27.1

## Installation

Go to root directory where `manage.py` is.

Install using `pip`...

    pip install -r pip-requirements.txt

# Now if you want to run

## 1. Wordle Clone Terminal ( Wordle Clone which runs in terminal )

Then, go to folder `wordle-terminal` and run using...

    python assignment.py

**NOTE: You Need Internet To Run This Code. In Case There Is No Internet, The Code Will Still Run But With Limited Words**


## 2. Wordle Clone API ( For Wordle Clone Frontend )

Then, run command...

    python manage.py runserver

and that's it, we're done!

**NOTE: You can also open the API in your browser at `http://127.0.0.1:8000/api/get-wordle/`, `http://localhost:8000/api/check-wordle/<GUESSED_WORD>/<CORRECT_WORD_PK_FROM_GET_WORDLE_API>/<NUMBER_OF_TRIES_MADE_RANGE_1_TO_6>/`, and view your API.**