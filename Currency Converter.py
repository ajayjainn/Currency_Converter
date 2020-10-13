# A GUI based application which converts INR to different currencies(using Tkinter).
from tkinter import Tk, Label,  Button, Entry, W

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
#Back End
def convert(currency_name, currency_value):
    global result, result_label
    answer = round(int(inr_input.get())/int(currency_value), 2)

    # Deleting result label and result.
    result_label.grid_forget()
    result.grid_forget()

    # Updating Result label and result with new value
    result_label = Label(root, text=currency_name, anchor=W)   # Result Label
    result_label.grid(row=2, column=0, padx=8, pady=8)
    result = Label(root, text=answer, anchor=W)                         # Result
    result.grid(row=2, column=1, padx=8, pady=8, columnspan=3)

def add_money(amount):
    previous = int(inr_input.get())                   # Storing Previous data
    inr_input.delete(0, 'end')                         # Clearing the text box
    inr_input.insert(0, previous + amount)      # Adding Previous Data and amount.

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Front End
root = Tk()
root.title("Currency Converter")

Label(root, text="INR", anchor=W).grid(row=1, column=0, padx=8, pady=8)
inr_input = Entry(root)
inr_input.grid(row=1, column=1, padx=15, columnspan=3)
inr_input.insert(0, 0)

result_label = Label(root, text="Currency", anchor=W)
result_label.grid(row=2, column=0, padx=8, pady=8)
result = Label(root, text="0")
result.grid(row=2, column=1, columnspan=3)

# Button which will add amount to inr_input.
Button(text="Add 100", command=lambda: add_money(100)).grid(row=0, column=1, pady=5, padx=5)
Button(text="Add 500", command=lambda: add_money(500)).grid(row=0, column=2, pady=5, padx=5)
Button(text="Add 1000", command=lambda: add_money(1000)).grid(row=0, column=3, pady=5, padx=5)

# Creating Currency Buttons
Button(root, text="Pound", padx=5, pady=5, command=lambda: convert('Pound', 90 )).grid(row=3, column=0, padx=10, pady=20)
Button(root, text="Euro", padx=5, pady=5, command=lambda: convert('Euro', 80)).grid(row=3, column=1, padx=10, pady=20)
Button(root, text="Dollar", padx=5, pady=5, command=lambda: convert('Dollar', 70)).grid(row=3, column=2, padx=10, pady=20)


root.mainloop()

