import random

# Word list
word_list = ['python', 'shadow', 'internship', 'developer', 'program', 'function']

# Choose a random word
word = random.choice(word_list)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!\n")

# Game loop
while attempts > 0:
    display_word = ''.join([char if char in guessed_letters else '_' for char in word])
    print(f"Word: {display_word}")
    
    if '_' not in display_word:
        print("🎉 Congratulations! You've guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!\n")
    else:
        attempts -= 1
        guessed_letters.append(guess)
        print(f"Wrong guess. Attempts left: {attempts}\n")

else:
    print(f"💀 Game Over! The word was: {word}")
