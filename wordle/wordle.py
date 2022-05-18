class WordleLetterStatus:
    CORRECT_LETTER_WITH_CORRECT_LOCATION: str = "CORRECT_LETTER_WITH_CORRECT_LOCATION"
    CORRECT_LETTER_WITH_INCORRECT_LOCATION: str = "CORRECT_LETTER_WITH_INCORRECT_LOCATION"
    WRONG_LETTER: str = "WRONG_LETTER"

class WordleStatus:
    CORRECT: str = "CORRECT"
    KEEP_TRYING: str = "KEEP_TRYING"
    FAILED: str = "FAILED"
    INTERNAL_ERROR: str = "INTERNAL_ERROR"
    INCOMPLETE_LETTERS: str = "NUMBER_OF_LETTERS_ARE_INCORRECT"

class Wordle:

    original: str = None

    guess: str = None

    tries: int = 0

    MAX_TRIES: int = 6

    def __init__(self, original, guess, tries) -> None:
        self.original = original.upper()
        self.guess = guess.upper()
        self.tries = tries

    def get_wordle(self):
        output_word = list()
        for i in range(0, len(self.original)):
            if self.guess[i] == self.original[i]: # check for letter in exact location
                output_word.append({
                    'letter': self.guess[i],
                    'state': WordleLetterStatus.CORRECT_LETTER_WITH_CORRECT_LOCATION
                })
            elif self.guess[i] in self.original: # if above condition fails that means character at this location (i) is not same, hence checking it for any other location
                output_word.append({
                    'letter': self.guess[i],
                    'state': WordleLetterStatus.CORRECT_LETTER_WITH_INCORRECT_LOCATION
                })
            else: # letter is nowhere to be found in the word
                output_word.append({
                    'letter': self.guess[i],
                    'state': WordleLetterStatus.WRONG_LETTER
                })
        return output_word

    def get_status(self):

        if self.tries > self.MAX_TRIES or self.tries < 1:
            return WordleStatus.INTERNAL_ERROR
        
        if self.guess == self.original:
            return WordleStatus.CORRECT

        if self.tries < self.MAX_TRIES:
            return WordleStatus.KEEP_TRYING
        else:
            return WordleStatus.FAILED