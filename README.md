# Guess the Word

A simple Hangman-style word-guessing game written in Python.

## About

The game picks a random word from a list, asks the player to guess a letter,
and shows the word as blanks with every correctly guessed letter revealed in
its position (e.g. guessing `p` in `apple` shows `_pp__`).

This is the beginning of the project; more features will be added step by step.

## Requirements

- Python 3

## How to run

```bash
python3 main.py
```

## Example

```
aardvark
________
Guess a letter: a
a
aa___a__
```

## Progress

- [x] Pick a random word from a word list
- [x] Ask the player for a lowercase letter guess
- [x] Check the guess against each letter in the word
- [x] Create a placeholder of blanks (`_____`), one per letter
- [x] Reveal correctly guessed letters in their positions
- [ ] Let the player keep guessing until the word is complete
- [ ] Add lives and a win/lose message
