# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Initially when I ran a new game I noticed the incorrect hints. At first I thought it said the opposite of what you should do but I found it seemed more random than that. For example, when the secret number was 74 and I guessed 9, it incorrectly said "Go LOWER" but when I guessed 8, it correctly said "Go HIGHER".

The next bug I noticed was discrepancy between the Developer Debug Info score and the Final score displayed upon the correct guess. In my case, 5 attempts listed a Developer Debug score of -10. Instead, the Final score listed to the player was 20.

Third, I noticed the broken New Game button. Trying to start a new game would show the player "You already won. Start a new game to play again." instead of actually starting a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code and had it plan a fix for the incorrect hints and then when I saw that the plan looked good I had it execute the plan. Then I had it write some tests in the test folder and this is where Claude showed its first inconsistency. 

Initially when I did Phase 2 Step 3 of the assignment and asked Claude to write a pytest in the tests folder, since there was already a test file with three incorrect tests in there that came with the starter code it fixed them and added two more new tests specifically targeting the incorrect hints. While that fixed the starter code tests, I wanted to understand more clearly the changes it made so I pasted back in the starter code test and asked Claude the main difference between that code and the five test version. Basically the five test version is a more complex fix that covers more cases. This example was a reminder that you have to be specific in how simple or complex you want your solution to give or else AI will just assume.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Manually testing by playing the game again was the most surefire way for me to decide if the bug was fixed. For example, the test I ran for seeing if the new game button worked was to go back onto the localhost site and try to start a new game. As stated in the previous answer, Claude helped design both a simple and a more complex pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

In fixing the New Game button not working as intended, I learned that Streamlit runs the whole script fresh top to bottom each time UNLESS a session state is updated because that's the only thing that persists between runs. A new game wasn't starting upon button click because nothing in the code changed the game status from a win back to a new fresh game with a new secret number and attempts. I would tell my friend to just be mindful of what is getting reset on a rerun and what explicitly stays between runs.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I've never had AI write tests for me before and always manually tested previously. I want to learn techniques that will help me trust the tests that AI design more without me manually testing each time. 

The discrepancy in the complexity in two of the tests that Claude wrote worries me so something I would do differently next time is specify how simple/complex I want the test to be.

AI generated code worked pretty well for simple mistakes like the higher or lower hints but people are still needed to keep AI in check because there are still plenty of ways that AI can assume things and get the intended design wrong. I'm looking forward to seeing AI attempting to fix more complicated problems in bigger projects.