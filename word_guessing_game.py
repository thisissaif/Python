import random

def get_random_word():
    # Example dictionary of words
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def word_guessing_game():
    word_to_guess = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word_to_guess)} letters. You have {attempts} attempts to guess it.")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! {guess} is not in the word. You have {attempts} attempts left.")
        
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

word_guessing_game()