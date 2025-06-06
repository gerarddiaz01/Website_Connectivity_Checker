import tkinter as tk
from tkinter import messagebox
import urllib.request
import urllib.error
import threading

# Button function
def check_connectivity():
    '''This function will be executed when the "Check" button is clicked'''
    url = url_entry.get().strip()  # Get text from the Entry widget and remove leading/trailing spaces to make sure is clean

    # Basic validation
    if url == "":
        # If the input is empty, show an error message in the result label
        result_label.config(text="❌ Please enter a URL.", fg="red") # config() is used to modify widgets properties dynamically
        return # Exit
    if "." not in url:
        # If the input doesn't contain a dot, it's likely not a valid URL
        result_label.config(text="❌ That does not look like a valid URL.", fg="red")
        return

    # Normalize the URL
    if not url.startswith("http://") and not url.startswith("https://"):
        # If the URL doesn't start with "http://" or "https://", add "https://"
        url = "https://" + url

    # Update the result label to indicate the URL is being checked
    result_label.config(text="Checking...", fg="Black") # fg to set text color

    # Launch the connectivity check in a new thread
    thread = threading.Thread(target=check_in_thread, args=(url,))
    thread.start() # Starts the thread, allowing the check_in_thread() function to run in the background

def check_in_thread(url):
    '''This function runs in a separate thread to check connectivity in the background'''
    try:
        # Send HTTP request
        response = urllib.request.urlopen(url, timeout=5)  # Timeout after 5 seconds if the server is unresponsive
        code = response.getcode()  # Get the HTTP status code

        # Check the status code
        if code == 200: # 200 means the site is accessible
            update_result("✅ Site is accessible (Code 200)", "green")
        else:
            update_result(f"⚠️ Site responded with code {code}", "orange")
    except urllib.error.HTTPError as e:
        # Handle HTTP errors (e.g., 404, 500)
        update_result(f"❌ HTTP Error: {e.code} - {e.reason}", "red")
    except urllib.error.URLError as e:
        # Handle URL errors (e.g., unreachable server)
        update_result(f"❌ URL Error: {e.reason}", "red")
    except Exception as e:
        # Handle any other unexpected errors
        update_result(f"❌ Unknown error: {e}", "red") # We call for update_result with the .config() method to update the widget

def update_result(message, color):
    '''Safely update the result label from a background thread with .config()'''
    root.after(0, lambda: result_label.config(text=message, fg=color)) # lambda function to pass to .config() the text and colors

def clear_fields():
    '''Clear the input field and reset the result label'''
    url_entry.delete(0, tk.END)  # Clear the text in the Entry widget
    result_label.config(text="")  # Reset the result label
    url_entry.focus()  # Auto-focus the Entry widget, so the user can start typing straight away

# Main window
root = tk.Tk()
root.title("Website Connectivity Checker")
root.geometry("400x200") # Size in pixels

# Label Widget
label = tk.Label(root, text="Enter website URL:", font=("Arial", 12))
label.pack(pady=10) # pack() is a layout manager in tkinter to automatically position widgets to the window

# Entry Widget for URL
url_entry = tk.Entry(root, width=50) # input field for the user to type the website URL
url_entry.pack(pady=5) # pady() is used to apply vertical padding, in this case 5 pixels

# Result Label Widget
result_label = tk.Label(root, text="", font=("Arial", 12)) # The text here will be updated dynamically with .config() after
result_label.pack(pady=10) # vertical padding creates space on top and below the object to be visually appealing

# Button Widget linked to the check_connectivity() function
check_button = tk.Button(root, text="Check", command=check_connectivity)
check_button.pack(pady=10)

# Button Widget linked to the clear_fields() function
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=2)

# Bind the Return (Enter) key to the check_connectivity function
root.bind('<Return>', lambda event: check_connectivity())

# Auto-focus the Entry widget when the app starts
url_entry.focus()

# Start the GUI Loop
root.mainloop()