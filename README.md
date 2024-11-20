# Wordle Solver

This Wordle Solver helps narrow down the possible 5-letter words based on constraints set by the user. It uses a list of all 5-letter words and dynamically filters them to suggest possible answers.

Github: [link](https://github.com/camy-code/ScreamingChessClock)

Youtube: [link](https://www.youtube.com) (still need to make video, sorry!)

## How It Works

- Word Selection: A file loads a list of all 5-letter words.
- Filtering Logic: The solver removes words from the list according to the constraints entered.

## Constraints

The solver uses the following constraints, updated after each guess:

- cor_placement: A dictionary where keys are positions and values are letters that must be in those exact positions.
- wrong: A set of letters not in the word.
- contain: A set of letters in the word but not in the given positions.
- wrong_placement: A dictionary where keys are letters and values are lists of positions where the letter should not appear.

## File Structure
- main.py: Deals with all the text handling as this is only a text interface app!
- wordle.py: Handles all the logic for word filtering based on constraints.
- bulk_word.py: The logic I used to get all the 5 letter words from all the words in the world! (That is what the link of world_list.txt at least said when I found it online!)

## Executing the program
Instructions are in main.

To run the code, please clone the repo and run main. There are some commented lines that one can uncomment to look at the commands of the program without needing to input the commands with a keyboard! These lines 63-83