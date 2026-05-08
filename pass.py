# Password Strength Checker using Tkinter

import tkinter as tk

# Function to check password strength
def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result.config(text="Please enter a password", fg="red")
    elif length < 5:
        result.config(text="Weak Password", fg="red")
    elif length < 8:
        result.config(text="Medium Password", fg="orange")
    else:
        result.config(text="Strong Password", fg="green")


# Create window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

# Label
label = tk.Label(window, text="Enter Password:")
label.pack(pady=10)

# Password Entry
entry = tk.Entry(window, show="*", width=25)
entry.pack(pady=5)
button = tk.Button(window, text="Check Strength", command=check_strength)
button.pack(pady=10)
result = tk.Label(window, text="")
result.pack(pady=10)
window.mainloop()