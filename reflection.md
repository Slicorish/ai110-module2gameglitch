# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

1. The hints telling me to go lower/higher were incorrect. I guessed 3 and was told to go lower, while the number was revealed to apparently be 36
2. Starting a new game button didn't work
3. "pressing enter to apply" didn't work, I had to actually press the submit guess button

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

* I used Claude Code on this project 
* One suggestion that the AI gave regarding Bug #1 that was correct was regarding the logic for the hint functions. The messages were saying if guess was too high, to go higher and if guess was too low, to go lower. In addition, there was an issue with an except type error in the check_guess function. The guess was being cast to a string when it just needed to stay as an integer. The try/except block wasn't needad altogether.
* I wouldn't say that any of the suggestions were incorrect, I just needed to ask for more clarification to understand the type Error and the try/except block issue

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

BUG 1: 
* I decided the bug was really fixed by first prompting claude to confirm and run test cases in the terminal, and then by re-running the application live, which then adjusted accordingly and performed the expected correct output. In this case in particular, the hints for guesses to go higher and lower now worked correctly. I then added test cases to test/tes_game_logic.py and ran pytest in the terminal and all of the test cases passed successfully
* One test I ran manually on the actual website was doing a live demo focusing on the check_guess and hints features. 
    - Guess 1: 50 --> hint is go Higher
    - Guess 2 : 60 --> hint is go Lower
    - Guess 3: 55 --> hint is go Higher
    - Guess 4: 57 --> hint is go Higher
    - Guess 5: 59 --> hint is go Lower
    - Guess 6: 58 --> correct guess!!
    - Success!!


BUG 2: 
* I decided the bug was at first not completely fixed after the first round of edits that claude had suggested and I implemented. I re-ran the application live to verify this. I had to use the develper debug info to verify that a new game was indeed started, but the field for you to guess a new number does not clear so the last guess is still there.

* The test I ran manually after making the second level of improvements was: 
- Guess 1: 50 --> hint is go Higher
- Guess 2: 90 --> hint is go Lower
- Guess 3: 80 --> hint is go Lower
- Guess 4: 70 --> correct game won
- Press New Game Button : text box refreshes and cleared previous output
- Success!!

* After I implemented another round of edits, the new game button does work as expected now and the text box refreshes. I checked the developer debug info again to confirm that a new game was started.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

By default, Streamlit acts like a clean slate on every interaction, and session state is the memory that prevents it from forgetting everything

On every rerun, ordinary Python variables are completely wiped and re-initialized. If you have x = 0 at the top of your script and a button that does x += 1, clicking that button triggers a rerun. The script starts from the top, sets x = 0 again, and your change is lost

Because reruns wipe ordinary variables, you need a way to remember data across those runs. Session State (st.session_state) is a dictionary-like object that persists data between reruns for a specific user session. A "session" is unique to each open browser tab. If User A and User B open your app, they each get their own isolated independent sandbox memory.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


* Attaching files directly for context in the chat is a habit/strategy that I will use for future labs and projects 

* One thing that I will do differently is ask for explanation when I ask about bugs in the code. I think that it's one thing to find out what/where the bug is, but also why the bug is an issue and what specifically about the logic and how it contributes to the functionality of the project as a whole. 

* One thing I will also do is to ask for specific line numbers of where claude is suggestion to add/remove code. This way I can double check and perform comparisons myself as well. This forces claude to show me the before and after version of my code. 