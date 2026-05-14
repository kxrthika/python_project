import tkinter as tk
import random
def play(user):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if user == computer:
        result.config(text="Tie! Computer chose " + computer)

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):

        result.config(text="You Win! Computer chose " + computer)

    else:
        result.config(text="You Lose! Computer chose " + computer)
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")
tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=5)
result = tk.Label(root, text="Choose one")
result.pack(pady=20)
root.mainloop()