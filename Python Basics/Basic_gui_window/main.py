from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Temperature Calculator")
window.minsize(width=250, height=130)
window.config(padx= 20,pady=20)

# Function to convert Fahrenheit to Celsius
def convert(fahrenheit_value):
    return (fahrenheit_value - 32) * 5 / 9

# Function to be called when button is clicked
def button_clicked():
    try:
        # Get the value from the Entry widget and convert it to float
        request = float(my_input.get())
        to_process = convert(request)
        result.config(text=f"{to_process:.2f} °C")  # Show result with 2 decimal places
        
    except ValueError: # Handeling errors
        result.config(text="Invalid input")

# Entry
my_input = Entry(width=30)
my_input.insert(END, string="Enter °F")
my_input.grid(row=0, column=1, pady=(10, 5), padx=5)

# Labels
description = Label(text="Is equal to:")
description.grid(row=1, column=0)

result = Label(text="")
result.grid(row=1, column=1)

fahrenheit = Label(text="°F")
fahrenheit.grid(row=0, column=2)

celsius = Label(text="°C")
celsius.grid(row=1, column=2)

# Button
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(row=2, column=1,)

# Start the GUI loop
window.mainloop()