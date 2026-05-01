import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = datetime.today()
        birth_date = datetime(year, month, day)

        age = today.year - birth_date.year

        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your Age is: {age} years")

    except:
        result_label.config(text="Invalid input!")

# Create window
root = tk.Tk()
root.title("Age Calculator")

# Labels and Entries
tk.Label(root, text="Day").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Year").grid(row=2, column=0)

entry_day = tk.Entry(root)
entry_month = tk.Entry(root)
entry_year = tk.Entry(root)

entry_day.grid(row=0, column=1)
entry_month.grid(row=1, column=1)
entry_year.grid(row=2, column=1)

# Button
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=3, column=0, columnspan=2)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Run app
root.mainloop()