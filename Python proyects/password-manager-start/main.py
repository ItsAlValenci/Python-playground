from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip 


file = "./data.json"
DEFAULT_EMAIL = "generic@outlook.com"

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def password_search():
    web_to_find = address.get().strip().lower() #we need to remove formatting
    try:
        with open(file, 'r') as password_file:
            passwords = json.load(password_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

    else:
        if web_to_find in passwords:
            found_email = passwords[web_to_find]["email"]
            found_password = passwords[web_to_find]["password"]
            messagebox.showinfo(title=web_to_find, message=f"Email: {found_email}\nPassword: {found_password}\n\nPassword coppied!")
            pyperclip.copy(found_password)
            reset_fields()
        else:
                messagebox.showwarning(title="Not found", message=f"No details for '{web_to_find.capitalize()}' found.")

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
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))] 

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
    website_value = address.get().lower()
    username_id = username.get().lower()
    password_value = password_info.get()

    new_data = {
        website_value:{
            "email": username_id,
            "password": password_value,
        }
    }

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Error", message= "Please make sure you typed your info.")
    else:
        message_info = f"Are you sure you want to save?\n User: {username_id}\n Password: {password_value}"

        is_ok = messagebox.askokcancel(title= f"Saving:{website_value}", message=message_info)

        if is_ok :
            try:
                with open(file, "r") as password_file:
                    #Read old data
                    password_data = json.load(password_file)

            except FileNotFoundError:
                 with open(file, "w") as password_file:
                    json.dump(new_data, password_file, indent=4)

            else:
                #Adding new info to data
                password_data.update(new_data)

                with open(file, "w") as password_file:
                    #Writing the update data to file 
                    json.dump(password_data, password_file, indent=4)

            finally:
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
address = Entry(width=21)
address.grid(column=1,row=1)
address.focus()


username = Entry(width=38)
username.grid(column=1,row=2, columnspan=2)
username.insert(0, DEFAULT_EMAIL)

password_info = Entry(width=21)
password_info.grid(column=1,row=3)


#Button
search_btn = Button(text="Search", width=13, command=password_search)
search_btn.grid(column=2,row=1)

generate_btn = Button(text="Generate Password", width=13, command=password_generator)
generate_btn.grid(column=2,row=3)

add_btn = Button(text= "Add", width=35, command=save)
add_btn.grid(column=1,row=4, columnspan=2)





window.mainloop()