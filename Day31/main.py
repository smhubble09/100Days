from random import choice
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
random_selection = {}
# ---------------------------- READ CSV ------------------------------- #
try:
    data = pandas.read_csv("Day31/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Day31/data/french_words.csv")  
finally:
    to_learn_dict = data.to_dict(orient="records")

# ---------------------------- REMOVE WORD ------------------------------- #
def remove_word():
    to_learn_dict.remove(random_selection)
    next_card()

# ---------------------------- PICK RANDOM WORD ------------------------------- #
def next_card():
    global random_selection, flip_timer
    window.after_cancel(flip_timer)
    #Random word selection
    random_selection = choice(to_learn_dict)
    #Change text
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_word, text=random_selection["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_timer = window.after(5000,change_card)

# ---------------------------- CHANGE CARD ------------------------------- #
def change_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_word, text=random_selection["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(5000,change_card)

#Images
card_back = PhotoImage(file="Day31/images/card_back.png")
card_front = PhotoImage(file="Day31/images/card_front.png")
wrong_img = PhotoImage(file="Day31/images/wrong.png")
right_img = PhotoImage(file="Day31/images/right.png")

canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_image = canvas.create_image(400,263, image=card_front)
canvas.grid(column=0,row=0, columnspan=2)
#Text in canvas
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

#Buttons
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(column=0,row=1)

right_button = Button(image=right_img, command=remove_word)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

df = pandas.DataFrame(to_learn_dict)
df.to_csv("Day31/data/words_to_learn.csv",index=False)