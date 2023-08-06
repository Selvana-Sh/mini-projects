from words import words
from hangman_visual import lives_visual_dict
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word: # invalid cases, keep iterating
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words) 
    word_letters = set(word)  

    # user part
    alphabet = set(string.ascii_uppercase) # what the user can choose from
    used_letters = set()  # what the user has guessed

    lives = 10
    while len(word_letters) > 0  and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        # get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters: # correct, unused letter
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # incorrect letter
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters: # correct,used letter
            print('\nYou have already used that letter. Guess another letter.')

        else: # invalid input
            print('\nThat is not a valid letter.')

    # dead
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    # guessed the word
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()