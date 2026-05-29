# Day 7: Hangman Game
#========================================
# Explanation of this project:
# This project is a simple hangman game 
# that takes the user's choices as input and outputs the result.
#========================================

import random

random_words = ["apple", "banana", "cherry", "date", "ball", "cat", "mouse"]

random_word = random.choice(random_words).lower()

place_holder = "_" * len(random_word)
print(place_holder)

lives = 4
while lives != 0 and "_" in place_holder:
    word = input("Guess the letter: ")
    if word in random_word:
        for i in range(len(random_word)):
            if random_word[i] == word:
                place_holder = place_holder[:i] + word + place_holder[i+1:]
    print(place_holder)
    if word not in random_word:
        lives -= 1
        print(f"You have {lives} lives left")
    if lives == 0:
        print("You lose!")
        break
    if "_" not in place_holder:
        print("You win!")
        break