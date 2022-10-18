#!/usr/bin/env python3

from random import randint

def user_input(prompt, lower_bound=0, upper_bound=0) -> int:
        need_integer = "You used a floating point Number!"
        need_number = "Your input wasn't a number!"
        while True:
            user_input = ""
            user_input = input(prompt)
            if user_input.upper() == "Q":
                quit()
            if len(user_input) == 0:
                continue
            try:
                user_number = int(user_input)
                if user_number == float(user_input):
                    if lower_bound == 0 == upper_bound:
                        return user_number
                    if lower_bound <= user_number <= upper_bound:
                        return user_number
                    print('That number was out of bounds')
                    continue
                else:
                    print('You used a float. Please use an integer')
                    continue
            except:
                print('I don\'t recognise that number. Please use an numeral')


class Guessing_game_round:
    """
    Game where the user must correctly guess a randomly generated integer between 1 and 100.
    User is told each time whether their guess is higher or lower.
    Uses the random library’s randint function.
    Q in general will quit.
    If you have found a bug you can try ctrl-d or ctrl-c
    """


    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.remaining_guesses = 11
        self.target = randint(self.lower_bound, self.upper_bound)
        self.guess = None
        self.won = False
        self.prompt = f'Please choose an integer between {self.lower_bound} and {self.upper_bound} (inclusive). '
        self.already_guessed = []

    def user_guess(self):
        self.guess = user_input(self.prompt, self.lower_bound, self.upper_bound)
        for previous in self.already_guessed:
            if self.guess == previous:
                self.remaining_guesses += 1
                print("You have already guessed that number before, press Q to quit")
                break
        else:
            self.already_guessed.append(self.guess)
        self.remaining_guesses -= 1
        print(f'{self.remaining_guesses} guesses remaining.')
        if self.guess < self.target:
            print("Higher")
        elif self.guess > self.target:
            print("Lower")
        else:
            self.won = True

    def play(self):
        while self.remaining_guesses > 0 and self.won is False:
            self.user_guess()
        if self.won is True:
            print(f'Congratulations! You won with {self.remaining_guesses} remaining')
        else:
            print(f'Not quite this time. The number was {self.target}')
        print('')


if __name__ == '__main__':
    game = Guessing_game_round()
    game.play()
