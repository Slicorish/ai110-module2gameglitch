# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

-  Game's purpose: the purpose of the game is to have a user guess a random number between 1 and 100. The user has 8 chances, the difficutly level can be adjusted, hints can be shown after each guess. The user can play multiple games. 
- I found 3 bugs: the hints guiding the user to guess higher or lower were incorrect; the new game button wasn't working and starting a new game when pressed; the enter button doesn't work when guessing, the user has to manually press the submit guess button
- I fixed 2/3 bugs. I fixed the hints feature and I fixed the new game feature

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User types a guess of 40 (guess 1)
2. User presses submit guess button (instead of pressing enter)
3. Hint go lower is given
4. User types a guess of 20 (guess 2)
5. User presses submit guess button
6. Hint go higher is given
7. User types guess of 30 (guess 3)
8. User presses submit guess button
9. Hint go higher is given
10. User types guess of 35 (guess 4)
11. User presses submit guess button
12. Guess was correct, user won game!
13. Attempts left counter says 4 attempts left
14. User presses New Game button
15. Text box to enter guess is cleared
16. Attempts left tracker is reset back to 8 and new game is started

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- I did not
