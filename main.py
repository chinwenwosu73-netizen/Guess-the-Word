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

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Print "Right" if it is, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
