# Website Connectivity Checker

This project is a Python-based GUI application that lets users check whether a website is accessible. Built with tkinter for the user interface and urllib for the connectivity logic, the app includes real-time feedback, validation, and threading for responsiveness.

What makes this project special is not just that it works — but that it explains how it works. The code is deeply commented, and a companion markdown file (Explanations.md) is included to teach beginners the core concepts behind threading, after(), and GUI-safe design.

---

## Teaching Perspective (For Beginners)

This project includes an extra markdown file, Explanations.md, that breaks down the logic behind:
   - How threading interacts with the tkinter event loop.
   - Why updating widgets from threads can crash your app.
   - What after() does and how it solves this.
   - Why we isolate result_label.config() into its own thread-safe function.

This project isn’t just something that works — it’s something you can learn from.

---

## Project Structure
Website_Connectivity_Checker/ 
├── src
    └──main.py    # Main script for the application 
├── README.md     # Project documentation
├── requirements.txt    # Libraries needed to run the code
└── Explanations.md     # Markdown file to explain about after(), threading and config()

---

## How to Run the Application

1. Make sure Python 3 is installed (python.org)
2. Run the following in terminal:
   python src/main.py
3. Then just:
   Enter a URL in the text field
   Click "Check" or press Enter
   See success/failure feedback instantly

---

## Features

- Input validation: Adds https:// if missing, prevents empty/invalid input
- Live GUI updates: Keeps UI responsive with threading
- Thread-safe widget updates: Uses after() to update labels safely
- Enter key support: Pressing Enter runs the check
- Clear button: Resets the form instantly
- Auto-focus on load: Lets you start typing immediately
- Color-coded feedback: Green for success, red for error

---

## Tools and Strategies Used

1. **`tkinter`**:
   - Used to create the graphical user interface, including labels, buttons, and input fields.
   - Demonstrates the use of layout managers like `pack()` and event bindings like `bind()`.

2. **`urllib`**:
   - Used to send HTTP requests and retrieve the status code of the given URL.
   - Handles errors like `HTTPError` and `URLError` gracefully.

3. **Thread-Safety**:
   - Ensures the GUI remains responsive by running the connectivity check in a separate thread.
   - Uses `root.after()` to safely update the GUI from the background thread.

4. **after()**
   - Schedules a function to safely update the GUI from a background thread. Used inside update_result() to modify the label with thread safety.

5. **update_result()**
   - A dedicated function that centralizes the result_label.config() call. Keeps code modular and safe from threading issues.

---

## Challenges Encountered and Solutions

1. Threading + GUI Safety
Problem: Direct widget updates from threads caused crashes.
Solution: Used after() to run result_label.config() on the main thread.

2. Input Handling
Problem: Users could submit empty or malformed URLs.
Solution: Added checks to clean/validate inputs. Automatically appends https:// if needed.

3. UI Freezing
Problem: The app froze while waiting for slow sites to respond.
Solution: Moved the request logic to a background thread.

4. Usability Polish
Problem: Clicking the input field every time was annoying.
Solution: Auto-focused the field at startup.

---

## What I Learned

This was one of the first projects where I combined real user interaction with background logic. I learned:
   - How to safely use threads in a GUI.
   - Why after() is critical for tkinter apps.
   - How to validate and clean user input.
   - How to structure code into functions and avoid duplication.
   - The value of commenting clearly for future learners.
   - Most importantly, I learned how to think like a user — keeping the UI clean, responsive, and intuitive.

---

## Conclusion

Building this website checker helped me grow from "knowing Python" to designing applications. It challenged me to understand how threads work with event loops, and how to structure interactive apps without freezing the GUI.

As always, the goal wasn’t to write perfect code — but to build something useful, reflect on the process, and share what I learned.

If you're a beginner looking to understand threading in tkinter: this project is for you.

