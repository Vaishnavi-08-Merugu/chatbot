## Bug Report

**Steps to reproduce:**
1. Open `blenderbot_chat.py`.
2. Run the script: `python blenderbot_chat.py`.
3. Enter input: "Hello" or any greeting.

**Expected behavior:**
The chatbot should respond with a greeting message like "Hello! How can I help you?" and continue the conversation without errors.

**Actual behavior:**
The program may crash or throw an error, e.g.,  
`IndexError: list index out of range`  
or the chatbot does not respond as expected.

**Environment:**
- OS: Windows 10 / Linux / MacOS (specify yours)
- Python version: 3.11
- GitLab project version: 0.1.0

**Additional context / Notes:**
- Ensure all dependencies are installed (`pip install -r requirements.txt`).
- The error may occur if the input is empty or unexpected.
- Screenshots or console logs can be attached here if needed.
