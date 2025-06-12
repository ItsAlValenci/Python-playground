from tkinter import *
from tkinter import messagebox
import random
import pyperclip 


file= "./data.txt"
DEFAULT_EMAIL = "generic@outlook.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    password_info.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_special = [random.choice(symbols) for char in range(random.randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4)
    )] 

    password_list = password_letters + password_special + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    password_info.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def reset_fields():
    address.delete(0, END)
    password_info.delete(0, END)

def save():
    new_address = address.get()
    new_username = username.get()
    new_password = password_info.get()

    if len(new_address) == 0 or len(new_password) == 0:
        messagebox.showerror(title="Error", message= "Please make sure you typed your info.")
    else:
        message_info = f"Are you sure you want to save?\n User: {new_username}\n Password: {new_password}"

        is_ok = messagebox.askokcancel(title= f"Saving:{new_address}", message=message_info)

        if is_ok :
            with open(file, "a") as password_manager:
                password_manager.write(f"\n{new_address} | {new_username} | {new_password} ")

            reset_fields()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx= 50,pady=50)


#canvas
canvas = Canvas(width= 200, height= 200, highlightthickness=0)
my_logo = PhotoImage(file= "logo.png")
canvas.create_image(130,90, image=my_logo )
canvas.grid(column=1,row=0)


# Labels
address_lb = Label(text="Website: ")
address_lb.grid(column=0,row=1)

User_lb = Label(text="Email/Username: ")
User_lb.grid(column=0,row=2)

password_lb = Label(text="Password: ")
password_lb.grid(column=0,row=3)


# Entries
address = Entry(width=38)
address.grid(column=1,row=1,columnspan=2)
address.focus()


username = Entry(width=38)
username.grid(column=1,row=2, columnspan=2)
username.insert(0, DEFAULT_EMAIL)

password_info = Entry(width=21)
password_info.grid(column=1,row=3)


#Button
generate_btn = Button(text="Generate Password", width=13, command=password_generator)
generate_btn.grid(column=2,row=3)

add_btn = Button(text= "Add", width=35, command=save)
add_btn.grid(column=1,row=4, columnspan=2)





window.mainloop()