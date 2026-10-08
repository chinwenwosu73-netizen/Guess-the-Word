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

# TODO-6 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
# all the letters in the chosen_word. At that point display has no more blanks ("_"), so tell the user they've won.
game_over = False
correct_letters = []

while not game_over:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Remember every correct guess so letters found in earlier rounds stay revealed.
    if guess in chosen_word:
        correct_letters.append(guess)

    # TODO-5 - Build the display: reveal each letter that has been guessed and put "_" in the rest.
    # e.g. if the user guessed "p" and the chosen word was "apple", display should be _pp__
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # No blanks left means every letter has been guessed.
    if "_" not in display:
        game_over = True
        print("You win!")
