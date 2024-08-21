import tkinter as tk

def calculate():
    num1 = int(entry_1.get())
    num2 = int(entry_2.get())
    operation = var.get()
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    else:
        result = num1 / num2
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.geometry("200x200")
root.title("Calculator")

var = tk.IntVar()

entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)

add_button = tk.Radiobutton(root, text="Add", variable=var, value=1)
subtract_button = tk.Radiobutton(root, text="Subtract", variable=var, value=2)
multiply_button = tk.Radiobutton(root, text="Multiply", variable=var, value=3)
divide_button = tk.Radiobutton(root, text="Divide", variable=var, value=4)

calculate_button = tk.Button(root, text="Calculate", command=calculate)

result_label = tk.Label(root)

entry_1.pack()
entry_2.pack()

add_button.pack()
subtract_button.pack()
multiply_button.pack()
divide_button.pack()

calculate_button.pack()

result_label.pack()

root.mainloop()
