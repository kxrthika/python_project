from tkinter import *
def calculate():
    p = float(principal.get())
    t = float(time.get())
    r = float(rate.get())
    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p

    result1.config(text="Simple Interest = " + str(round(si, 2)))
    result2.config(text="Compound Interest = " + str(round(ci, 2)))

root = Tk()
root.title("Interest Calculator")
root.geometry("350x300")
Label(root, text="Principal Amount").pack()
principal = Entry(root)
principal.pack()
Label(root, text="Time Period").pack()
time = Entry(root)
time.pack()
Label(root, text="Rate of Interest").pack()
rate = Entry(root)
rate.pack()
Button(root, text="Calculate", command=calculate).pack(pady=10)
result1 = Label(root, text="")
result1.pack()
result2 = Label(root, text="")
result2.pack()
root.mainloop()