"""
print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
      '''
) 
"""
import random

MAX_GUESSES = 10
NUM_DIGITS = 3


# generate valid answer
def getSecretNum():
    numbers = list(range(10))
    #random.shuffle(numbers)

    # get the first n digits
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def check_guess(answer, user_inputs):
    if answer == user_inputs:
        return "You got it!"

    clues = []

    for i in range(len(user_inputs)):
        # A correct digit in the correct position is a "Fermi".
        if (user_inputs[i] == str(answer[i])):
            clues.append('Fermi')
        elif str(user_inputs[i]) in map(str, answer):
            # a correct digit in wrong position
            clues.append('Pico')
   
    if len(clues) == 0:
        return "Bagels"
    else:
        # Sort clues to obscure which was correct and which was not.
        clues.sort()

        # Make a single string from the list of string clues.
        return ' '.join(clues)

                  
def main():
    while True:
        # generate valid answer
        answer = getSecretNum()
        
        # check the user's input
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            clues = check_guess(answer, guess)
            print(clues)

            numGuesses += 1

            if guess == answer:
                break # they are correct, so break out of this loop
            if numGuesses == MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {answer}.')
    
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')
        

if __name__ == '__main__':
    main()
        
    






