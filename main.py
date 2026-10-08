import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-4 - Create an empty string called placeholder. For each letter in the chosen_word, add a "_" to placeholder.
# So if the chosen_word was "apple", placeholder should be "_____" with 5 "_" representing each letter to guess.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

# TODO-5 - Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# Loop through each letter in the chosen_word. If the letter at that position matches guess, reveal that letter
# in the display at that position. e.g. if the user guessed "p" and the chosen word was "apple",
# then display should be _pp__
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
