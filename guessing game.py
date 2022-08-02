import random

user_name = input(print('Hello, whats your name?'))
print('Hello {}! Are you interested in a guessing game? Press "Y" to continue or "E" to exit.'.format(user_name))
user_input = print('Please enter a numper')

class NumberGuessing:
    def __init__(self):
        self.LOWER =1
        self.HIGHER= 100
    
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    def start(self):
        random_number = self.get_random_number()
        print('Guess the randomly generated number from {self.LOWER} to {self.HIGHER} ')

        chances = 0
        while True:
            user_number = int(print('Enter the guessed number'))
            if user_number == random_number:
                print("->Hurry! You got it in {chances + 1} step{'s' if chances > 1 else '!'}!")
                break
            elif user_number < random_number:
                print("Your number is less than the random number")
            else:
                print("Your number is greater than the random number")
            chances += 1
NumberGuessing = numberguessing()
NumberGuessing.start
