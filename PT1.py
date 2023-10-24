#!/usr/bin/env python3

# Author: Harrison Morrow
# Name: Programming Task 1
# Purpose: Given a list of digits determine the integer that it represents

import typing

def digit_list_reader(digit_list: list[int]) -> int:
    """
    Takes a list of decimal digits (digit list)
    Returns the integer the list represents
    """
    # Create our output
    output = 0
    # Reverse our list so we can work through each element from lowest decimal value to highest decimal value
    reversed_digit_list = list(reversed(digit_list))
    # Use a 'for' loop to loop over all positions in our list
    for i in range(len(reversed_digit_list)):
        current_digit = reversed_digit_list[i] # Get value of current digit
        output += current_digit * 10 ** i # Add that value to our output
    # Tell our caller the result of our calculation
    return output


if __name__ == '__main__':
    print(digit_list_reader([8,3,5,1]))

