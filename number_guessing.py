# The program imports the random module to generate a random number.

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    user_guess = None

# The guess_the_number function is defined to encapsulate the game logic.A random number between 1 and 100 is generated and stored in number_to_guess. 
    
    
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while user_guess != number_to_guess:
        try:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")


# The user is prompted to guess the number, with feedback provided after each guess:If the guess is too low, the program prints "Too low! Try again."If the guess is too high, the program prints "Too high! Try again."If the guess is correct, the program prints a congratulatory message.
# The while loop continues until the user guesses the correct number.

guess_the_number()