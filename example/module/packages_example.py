'''
Packages Assignment:  Guess the random number

Examine the number_guess() function, which should choose a 
random number between 1 and 100 by calling random.randint() and then output if the guessed number is too low, too high, or correct.

This imports the random module to use the random.seed() and random.randint() functions.

random.seed(seed_value) seeds the random number generator using the given seed_value.
random.randint(a, b) returns a random number between a and b (inclusive).
For testing purposes, use the seed value 100, which will cause the computer to choose the same random number every time the program runs.

Ex: If the input is:

32 45 48 80
the output is:

32 is too low. Random number was 80.
45 is too high. Random number was 30.
48 is correct!
80 is too low. Random number was 97.
'''

#import  your packages_module to have your main program gain access to number(guess)
import packages_module
import random

if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        print( packages_module.number_guess(num) )