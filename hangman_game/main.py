import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list).lower()

#Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

print(hangman_art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')


#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for letter in chosen_word:
    display.append('_')
#test
print(f"The word you have to guess is {' '.join(display)}.")

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word 
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False
wrong_list = []

while not end_of_game:
    
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input('Guess a letter: ').lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You have already guessed letter [{guess}]. Please try again.')

    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(f'There is/are {display.count(guess)} [{guess}] in the word.')

    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
    if guess not in chosen_word:
        if guess in wrong_list:
            print(f'But you have already guessed letter [{guess}]. Please try again!')
        else:    
            print(f'You lose a life. Please try again.')
            lives -= 1
        wrong_list += guess

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])

    if '_' not in display:
        end_of_game = True
        print("You guessed the word. You won!!")
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    elif lives <= 0:
        end_of_game = True
        print("You have used up all lives. You lost!")
        print(f"Your word is {chosen_word}.")