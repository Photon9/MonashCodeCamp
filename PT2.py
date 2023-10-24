#!/usr/bin/env python3

# Author: Harrison Morrow
# Title: Programming Task 2
# Purpose: A game where the user must correctly guess a randomly generated integer between 1 and 100.
# Goal of the design: Suitibly demonstrate abstraction while avoiding needless indirection

import typing
from random import randint

# All user input from python's "input" function is a string
# Only a subset of strings can be cast to an integer
# To ensure our program only deals with the user inputs we want we must validate our input
# Our program is meant to be about guessing numbers, not an input validator
# We will encapsulate our instructions for validating user input in a function that we will call from our guessing game function
# This will make our guessing game easier to understand

def int_input(low: int, high: int) -> int:
    """
    Takes a low and high integer
    Requests user input until user inputs integer between low and high
    Returns that input
    """
    # We request user input once
    request_string = f"Please enter an integer between {low} and {high}: "
    user_input = input(request_string)
    while True: # The user is stuck in this loop until they pass our conditions
        # casting can throw errors so we will use a try/except block
        try:
            # this ensures the user is not trying to trick us with floats
            if float(user_input) == int(user_input):
                return int(user_input)
        except:
            # Here we encourage our user to play by the rules with an informative error message
            error_string = f"Your input, {user_input}, was not an integer between {low} and {high}"
            print(error_string)
            user_input = input(request_string)


def guesser(low: int, high: int) -> None:
    """
    Randomly chooses a target integer between low and high
    Prompts user for input until user successfully guesses the target
    Advises user if guess is higher or lower than the target
    """
    target = randint(low, high)
    hint = "Your guess was" # This will eliminate semantic ambiguity in our hints that we print
    # Removing the following loop from our program would not have added to our program's readability
    while True: # The user is stuck in here until they guess correctly
        guess = int_input(low, high)
        if guess > target:
            print(hint, "higher")
        elif guess < target:
            print(hint, "lower")
        else: # this is only reached if our users guess is neither greater or less than the target
            break
    print("You won the game! Goodbye.")
    

if __name__ == '__main__':
    guesser(1, 100)
