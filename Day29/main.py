from tkinter import *
from tkinter import messagebox
from random import randint, choices, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(10, 12)
    nr_symbols = randint(2, 5)
    nr_numbers = randint(2, 5)

    password_list = [char for char in choices(letters, k=nr_letters)]
    password_list += [sym for sym in choices(symbols, k=nr_symbols)]
    password_list += [num for num in choices(numbers, k=nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    
    password_input.delete(0, END)
    password_input.insert(0, password)
    #Copy password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_input.get()
    email = email_input.get()
    site = website_input.get()

    if len(password) == 0 or len(email) == 0 or len(site) == 0:
        messagebox.showerror(title="Missing Field",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(title=site, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("Day29/Data.txt", mode="a") as data:
                data.write(f"{site} -> {email} -- {password}\n")

            password_input.delete(0, END)
            website_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

logo = PhotoImage(file="Day29/logo.png")

canvas = Canvas(height=200,width=200)
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Inputs
website_input = Entry(width=55)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=55)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"test@gmail.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=46, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()