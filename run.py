import random
from words import words
import string
from hangman import HANGMAN

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "left. You have guessed: ", "".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", "".join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                #print(HANGMAN[len(used_letters)])
                print(HANGMAN[lives])              
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You have already guessed this letter. Please guess again")

        else:
            print("Invalid")

    if lives == 0:
        print("You died. The word was ", word)
    else:
        print("Congratulations! You guessed the word was ", word)

if __name__ == '__main__':
    hangman()