from tkinter import *
from tkinter import messagebox
from random import randint, choices, shuffle
import pyperclip
import json
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

# ---------------------------- JSON FILE ------------------------------- #
def read_json(new_data):
    try:
        with open("Day29/data.json", mode="r") as data_file:
            #Reading old data
            data = json.load(data_file)    
    except FileNotFoundError:
        #Create new data file
        with open("Day29/data.json", mode="w") as data_file:
            #Saving data
            json.dump(new_data, data_file, indent=4)
        return data_file
    else:
        return data

def write_json(new_data, data):
    #Updating old data with new data
    data.update(new_data)
    with open("Day29/data.json", mode="w") as data_file:
        #Saving updated data
        json.dump(data, data_file, indent=4)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    data = read_json("")
    website = website_input.get()
    if website in data:
        username = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website,message=f"Username\Email: {username}\nPassword: {password}")
    else:
        messagebox.showinfo(title=website,message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_input.get()
    email = email_input.get()
    site = website_input.get()
    #Put data into dictionary
    new_data = {
        site: {
            "email": email, 
            "password": password
        }
    }

    if len(password) == 0 or len(email) == 0 or len(site) == 0:
        messagebox.showerror(title="Missing Field",message="Please don't leave any fields empty!")
    else:
        data = read_json(new_data)
        write_json(new_data, data)
        #Clear inputs
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
website_input = Entry(width=36)
website_input.grid(column=1, row=1)
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

search_button = Button(text="Search",width=15, command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()