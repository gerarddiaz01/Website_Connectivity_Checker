# Explanations:

**Threading**
Threading allows you to run multiple tasks concurrently within the same program. In the context of GUI applications like tkinter, 
threading is particularly useful because it helps keep the GUI responsive while performing long-running tasks.
It avoids freezing the GUI, because with tkinter the main thread is responsible for handling user interactions and updating the GUI.
While the main thread is handling long running tasks the GUI is frozen and will crash if you interact with it, by moving the long
running task to a separate thread we allow the main thread to be free to handle user interactions and update the GUI.
In the app we have...
    -Main thread: it runs the main loop event and handles user interactions.
    -Background thread: the threading.Thread object is used to run the connectivity check (check_in_thread()) in a separate thread.
    -Thread-Safe Updates: since tkinter is not thread-safe, you cannot directly update widgets (e.g., result_label) from a 
    background thread. Instead, you use root.after() to schedule updates on the main thread, ensuring thread safety.

**After() in tkinter**
The after() method in tkinter is used to schedule a function to be executed after a specified amount of time. 
It is particularly useful in GUI programming for tasks like:
Delaying Execution: Running a function after a delay (e.g., animations, timers).
Repeating Tasks: Scheduling a function to run repeatedly (e.g., updating a clock).
Thread-Safe Updates: Safely updating the GUI from a background thread.

- How It Works:
after() schedules the callback function to run on the main thread after the specified delay.
It does not block the main thread while waiting for the delay to complete.
If used with 0 as the delay, the function is executed as soon as the main thread is idle.

- Why It's Useful:
-Thread-Safety: tkinter is not thread-safe, so you cannot directly update widgets (like result_label) from a background thread. 
    Using after(), you can schedule the update to run on the main thread, avoiding crashes or undefined behavior.
-Non-Blocking: It allows the GUI to remain responsive while scheduling tasks.

**Why separate result_label.config() into another function?**
Separating result_label.config() into the update_result() function is necessary because:
    -Thread-Safety: result_label.config() directly modifies a tkinter widget, which must be done on the main thread. 
        The update_result() function uses after() to ensure this happens safely.
    -Reusability: By centralizing the logic for updating the result label, you avoid duplicating code. 
        If you need to change how the label is updated (e.g., adding logging or animations), you only need to modify update_result().