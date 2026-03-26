import random
random_words = ["apple", "banana", "cherry", "date", "ball", "cat", "mouse"]

guess_word = random.choice(random_words)
print(guess_word)  # For testing purposes; remove or comment out in production

placeholder = ""
for no_words in range(len(guess_word)):
    placeholder += "_"
print(placeholder)
game_over = False
while game_over == False:
    letters = input("Enter a letter to check if it's in the word: ").lower()

    display = ""

    for letter in guess_word:
        if letter == letters:
            display += letters
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("Congratulations! You've guessed the word:", guess_word)
        game_over = True
    