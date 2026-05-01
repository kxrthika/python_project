import tkinter as tk

# Function to calculate product
def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Product: " + str(result))

# Create window
root = tk.Tk()
root.title("Product Calculator")

# Labels and Entry boxes
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button
tk.Button(root, text="Calculate Product", command=calculate_product).pack()

# Result label
label_result = tk.Label(root, text="Product: ")
label_result.pack()

# Run the app
root.mainloop()