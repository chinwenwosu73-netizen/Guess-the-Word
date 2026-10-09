# Hangman in Python: 7-Day Beginner Study Guide

_Last updated: October 9, 2026_

## How to use this guide

Plan on 7 days at 1 to 2 hours a day to go from zero to building Hangman on your own. Each day teaches one idea, uses it in the game, and ends with a checklist. Don't start the next day until you can tick every box.

**Your daily routine (about 90 minutes)**

1. **Warm up (10 min):** without looking, retype yesterday's code from memory. Then check it against the guide.
2. **Learn (20 min):** read the day's concepts and watch the matching Udemy video.
3. **Practise (30 min):** do the day's practice exercises in a new PyCharm file.
4. **Build (20 min):** add the day's piece to your Hangman file and run it.
5. **Check (10 min):** go through the success checklist. Every box you can't tick goes on tomorrow's warm-up.

**Five rules**

- **Type, never copy and paste.** Your fingers learn the code as well as your eyes.
- **Run after every small change.** If something breaks, you'll know exactly which line caused it.
- **Explain it out loud.** If you can't explain a line in plain English, you don't know it yet.
- **Errors are normal.** Read the last line of the error message first. It names the problem.
- **Commit when it works.** Each working step goes to your Guess-the-Word GitHub repo, so you can see your progress.

**Your files:** create a folder in PyCharm called `Hangman` with one file per day: `day1.py`, `day2.py` and so on. Each day starts by copying the previous day's working file.

## Day 1: Plan the game, then learn variables, text and input

By the end of Day 1 you can describe the whole game in plain English and write a program that asks the player for a letter.

**1. Plan first (15 min, on paper, no code)**

Write the game in one paragraph: *The computer secretly picks a word. The player sees one blank per letter. The player guesses one letter at a time. Correct letters appear in their places. When no blanks are left, the player wins.* Then break it into numbered steps. This is called **decomposition**, and it's the first thing engineers do on any project.

**2. Concepts**

| Concept | Plain English | Example |
| --- | --- | --- |
| `print()` | Show something on screen | `print("Hello")` |
| Variable | A labelled box that stores a value | `name = "Ada"` |
| `=` | Put the right side into the box on the left | `guess = "a"` |
| String | Text, always inside quotes | `"camel"` |
| `input()` | Ask the player to type, and get back what they typed | `input("Your name? ")` |
| `.lower()` | Make text lowercase | `"A".lower()` gives `"a"` |
| Comment `#` | A note for people; Python ignores it | `# pick a word` |

**3. Practice (in `practice1.py`)**

1. Print your name and your favourite food on two lines.
2. Ask the user for their name and print `Hello, ` followed by it.
3. Ask for a word, convert it to lowercase, and print it.
4. Make the error `NameError` happen on purpose by printing a variable you never created. Read the message.

**4. Build (in `day1.py`)**

```python
# Ask the user to guess a letter and make it lowercase
guess = input("Guess a letter: ").lower()
print(guess)
```

**5. Success checklist: Day 1**

- [ ] I wrote the game's plan and its numbered steps on paper without help
- [ ] I can explain the difference between a variable and a string
- [ ] I can explain why `=` means "store" and not "equals"
- [ ] I wrote the Day 1 build code from memory and it runs
- [ ] Typing `P` prints `p`, and I can say which part of the code did that
- [ ] I caused a `NameError` and can explain what it means

## Day 2: Lists and picking a random word

By the end of Day 2 your program secretly picks a word from a list.

**1. Concepts**

| Concept | Plain English | Example |
| --- | --- | --- |
| List | Many values in one box, in order, inside `[ ]` | `["aardvark", "baboon", "camel"]` |
| Index | A position in a list, counted from 0 | `word_list[0]` is `"aardvark"` |
| Module | A ready-made toolbox that comes with Python | `random` |
| `import` | Open a toolbox so you can use it | `import random` |
| `random.choice()` | Pick one item from a list at random | `random.choice(word_list)` |
| `len()` | Count the items in a list, or the letters in a word | `len("camel")` gives `5` |

**2. Practice (in `practice2.py`)**

1. Make a list of 5 fruits and print the first and last one using their index.
2. Print how many fruits are in the list with `len()`.
3. Use `random.choice()` to print a random fruit. Run it 5 times and watch it change.
4. Delete the `import random` line, run it, and read the error. Put the line back.

**3. Build (in `day2.py`, starting from a copy of `day1.py`)**

```python
import random

word_list = ["aardvark", "baboon", "camel"]

# Pick a random word. Print it for testing only.
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)
```

`import` lines always go at the very top of the file.

**4. Success checklist: Day 2**

- [ ] I can create a list and read any item by its index
- [ ] I can explain why the first item is at index 0
- [ ] I can explain what `import random` does and what happens without it
- [ ] Running `day2.py` several times prints different words
- [ ] I wrote the Day 2 build code from memory
- [ ] I added 3 new words to `word_list` and the game still runs

## Day 3: For loops and showing the blanks

By the end of Day 3 the game shows one underscore per letter, like `_____` for "camel".

**1. Concepts**

| Concept | Plain English | Example |
| --- | --- | --- |
| `for` loop | Repeat some lines a set number of times | `for letter in "cat":` runs 3 times |
| Loop variable | Holds the current item on each pass | `letter` is `c`, then `a`, then `t` |
| `range(n)` | The numbers 0 up to n-1 | `range(5)` gives 0, 1, 2, 3, 4 |
| Indentation | 4 spaces that say "this line is inside the loop" | the line under `for ...:` |
| `:` | "A block starts here"; the next lines must be indented | `for i in range(3):` |
| `+=` | Add to what's already there | `text += "_"` |
| Empty string | Text with nothing in it yet | `""` |

**2. Practice (in `practice3.py`)**

1. Print each letter of your name on its own line with a `for` loop.
2. Print the numbers 0 to 9 with `range(10)`.
3. Start with `stars = ""` and use a loop to make it `*****`.
4. Move `print(stars)` inside the loop (indent it). Run it and explain why the output changed.
5. Remove the indentation from the line inside a loop and read the `IndentationError`.

**3. Build (add under `chosen_word` in `day3.py`)**

```python
# One "_" for each letter in the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
```

**4. Success checklist: Day 3**

- [ ] I can explain what `range(5)` produces and why it stops at 4
- [ ] I can explain why `print(placeholder)` is not indented
- [ ] I can write the placeholder loop from memory
- [ ] For "aardvark" the game prints exactly 8 underscores
- [ ] I can trace the loop on paper for "camel", showing `placeholder` after each pass
- [ ] I caused an `IndentationError` and fixed it

## Day 4: Decisions with if, elif and else

By the end of Day 4 one guess is revealed in the right places, so guessing `p` in "apple" shows `_pp__`.

**1. Concepts**

| Concept | Plain English | Example |
| --- | --- | --- |
| `if` | Run the indented lines only when something is true | `if age >= 18:` |
| `else` | Otherwise, run these lines | `else:` |
| `elif` | "Else if": checked only when the `if` above was false | `elif age >= 13:` |
| `==` | Compare: are these equal? (one `=` stores, two `==` compare) | `letter == guess` |
| `!=` | Are these different? | `guess != ""` |
| `in` | Is it inside? | `"a" in "camel"` is `True` |
| `not in` | Is it not inside? | `"_" not in "camel"` is `True` |

Python checks `if`, then each `elif`, then `else`, and runs **only the first one that's true**.

**2. Practice (in `practice4.py`)**

1. Ask for a number. Print `Big` if it's over 100, otherwise `Small`. Tip: `int(input(...))` turns typed text into a number.
2. Ask for an age and print `Child` (under 13), `Teen` (13 to 17) or `Adult` using `if / elif / else`.
3. Ask for a letter and print whether it's in the word `"python"`, using `in`.
4. Write `if letter = guess:` (one `=`), run it, and read the `SyntaxError`.

**3. Build (replace your old guess check in `day4.py`)**

```python
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
```

**4. Success checklist: Day 4**

- [ ] I can explain the difference between `=` and `==` without looking
- [ ] I can explain when the `elif` line is checked and when it's skipped
- [ ] I can write the display loop from memory
- [ ] With "camel" and the guess `a`, the game prints `_a___`
- [ ] I can trace the loop on paper for "apple" and `p`, showing `display` after each letter

## Day 5: While loops, true/false and memory

By the end of Day 5 you have a complete, winnable game: the player keeps guessing, earlier letters stay revealed, and the game says "You win!"

**1. Concepts**

| Concept | Plain English | Example |
| --- | --- | --- |
| Boolean | A value that is only `True` or `False` | `game_over = False` |
| Flag | A boolean used as an on/off switch | `game_over` |
| `not` | Flips true and false | `not False` is `True` |
| `while` loop | Repeat until something changes; you don't know how many times | `while not game_over:` |
| `.append()` | Add an item to the end of a list | `correct_letters.append("a")` |
| Empty list | A list with nothing in it yet | `[]` |

**`for` or `while`?** Use `for` when you know how many times to repeat (once per letter). Use `while` when you're waiting for something to happen (until the player wins).

**Where variables go:** anything that must be remembered between rounds (`game_over`, `correct_letters`) is created **before** the `while` loop. If you put it inside, it's reset every round.

**2. Practice (in `practice5.py`)**

1. Count from 1 to 5 with a `while` loop and a counter that goes up by 1 each time.
2. Keep asking "Say yes: " until the user types `yes`, using a flag.
3. Start with `fruits = []`, ask for 3 fruits, `.append()` each one, then print the list.
4. Write a `while` loop that never ends, then stop it with PyCharm's red ■ button. Explain why it never ended.

**3. Build (in `day5.py`)**

```python
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
```

**4. Success checklist: Day 5**

- [ ] I can explain when to use `while` and when to use `for`
- [ ] I can explain why `correct_letters = []` must be above the `while` line
- [ ] I can explain what the `elif letter in correct_letters` line fixes
- [ ] I won a full game, and earlier letters stayed revealed every round
- [ ] A wrong guess just shows the same display again, with no error
- [ ] I can say exactly which line ends the loop, and how

## Day 6: Rebuild the whole game from a blank file

Day 6 is the real test: you rebuild the complete game in a new, empty file without looking at any notes.

**1. The rebuild (45 min)**

1. Open a new file called `rebuild.py`. Close this guide and your old files.
2. Write your plan as `#` comments first, one comment per step.
3. Write the code under each comment. Run the file after each step.
4. When you're stuck for more than 10 minutes, look at **one** line only, then close it again. Write down which line it was, because that's tomorrow's warm-up.

**2. Debugging practice (30 min)**

Break your working game on purpose, one change at a time. Predict the result, run it, read the error, then fix it.

| Break it like this | What happens |
| --- | --- |
| Delete `import random` | `NameError: name 'random' is not defined` |
| Move `chosen_word = ...` below the `while` loop | `NameError: name 'chosen_word' is not defined` |
| Remove the indent under `for letter in chosen_word:` | `IndentationError: expected an indented block` |
| Write `if letter = guess:` | `SyntaxError` |
| Move `correct_letters = []` inside the `while` loop | No error, but earlier letters disappear each round |
| Delete `.lower()` and guess a capital letter | No error, but the guess never matches |
| Delete `game_over = True` | No error, but the game never ends |

The last three are **logic bugs**: no error appears, but the program does the wrong thing. They're the hardest kind to spot, and the best way to find them is to trace the code on paper.

**How to read any error:** start at the **last line**. It names the error type and the problem. The line just above it shows the file and line number where Python stopped.

**3. Success checklist: Day 6**

- [ ] I rebuilt the full game in a blank file in under 45 minutes
- [ ] I looked at notes 2 times or fewer
- [ ] I can predict all 7 results in the table before running them
- [ ] For any error, I can find the line number and say what's wrong
- [ ] I can explain the difference between an error and a logic bug

## Day 7: Add lives, a way to lose, and save to GitHub

By the end of Day 7 the player has 6 lives, loses one per wrong guess, and can lose the game. You design this part yourself using only ideas you already know.

**1. Plan it first (on paper)**

Answer these before writing any code:

1. Where should `lives = 6` be created: before the loop or inside it? Why?
2. How do you know a guess was wrong? (Hint: `not in`.)
3. What should happen when `lives` reaches 0?
4. What should happen if the player guesses a letter they've already found?

**2. Build it (in `day7.py`)**

Add these one at a time and run the game after each:

1. Create `lives = 6` in the right place.
2. After the display is printed, check whether the guess was wrong. If it was, take away one life with `lives -= 1` and print how many are left.
3. If `lives` is 0, set `game_over = True` and print `You lose. The word was` followed by the chosen word.
4. Before checking the guess, tell the player if they already guessed that letter.
5. Remove `print(chosen_word)` so the word is secret again.

The Udemy course's next videos add these same features plus ASCII art. Try your own version first, then compare.

**3. Save it to GitHub**

Copy your finished game into `main.py` in your Guess-the-Word project. In PyCharm, press **Cmd+K**, write a short message such as `Add lives and lose condition`, and click **Commit and Push**.

**4. Success checklist: Day 7**

- [ ] I answered all 4 planning questions before writing code
- [ ] A wrong guess takes away exactly one life and shows how many are left
- [ ] Losing all 6 lives ends the game and shows the word
- [ ] Winning still works and says "You win!"
- [ ] Repeating a letter tells the player they already guessed it
- [ ] The finished game is committed and visible on GitHub

## Ready for the next Udemy lesson?

Move on when you can tick at least 9 of these 10 boxes. If you can tick 7 or fewer, repeat Day 6 (the rebuild) once more first.

**Can you build it?**

- [ ] I can build the full winnable game from a blank file in under 30 minutes, without notes
- [ ] I added lives and a lose message on my own
- [ ] I can fix a `NameError`, `IndentationError` and `SyntaxError` by reading the message

**Can you explain it?** (Explain each one out loud, in plain English, in under a minute.)

- [ ] What a variable, a string, a list and a boolean are, with one example each
- [ ] The difference between `=` and `==`
- [ ] When to use a `for` loop and when to use a `while` loop
- [ ] How `if / elif / else` decides which lines run
- [ ] Why `correct_letters` is created before the `while` loop

**Can you use it somewhere new?**

- [ ] I built one small program that isn't Hangman using loops and `if`, such as a number-guessing game where the computer picks a number from 1 to 100 and says "higher" or "lower"
- [ ] I changed the game on my own in some way, such as a longer word list or a "Play again?" question

## Cheat sheet

Keep this open next to PyCharm while you practise.

**Symbols and keywords**

| Write | Meaning |
| --- | --- |
| `=` | Store a value in a variable |
| `==` / `!=` | Compare: equal? / different? |
| `+=` / `-=` | Add to / take away from what's already there |
| `" "` | Text (a string) |
| `[ ]` | A list |
| `( )` | Give something to a function: `len(word)` |
| `:` | A block starts here, so indent the next lines |
| `#` | A comment, ignored by Python |
| `in` / `not in` | Is it inside? / Is it not inside? |
| `True` / `False` | The two boolean values |
| `not` | Flips `True` and `False` |
| `.lower()` / `.append()` | Methods: actions a value can do to itself |

**Common errors**

| Error (last line of the message) | What it usually means | Fix |
| --- | --- | --- |
| `NameError: name 'x' is not defined` | The variable is never created, is created lower down, or is misspelt | Create it above the line that uses it and check the spelling |
| `IndentationError` | A line inside a block isn't indented, or the spacing is uneven | Indent with exactly 4 spaces per level |
| `SyntaxError` | Python can't read the line: often a missing `:`, quote or bracket, or `=` instead of `==` | Check the line it points to and the one above |
| `TypeError` | Two kinds of value used together wrongly, like text + number | Convert with `int()` or `str()` |
| `IndexError: list index out of range` | Asked for a position the list doesn't have | Remember positions start at 0 and end at `len(list) - 1` |

Your code so far lives at [github.com/chinwenwosu73-netizen/Guess-the-Word](https://github.com/chinwenwosu73-netizen/Guess-the-Word).
