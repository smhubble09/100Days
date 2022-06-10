from tkinter import *

window = Tk()
window.title("Kilometer to Miles Converter")
#window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

def calculate():
    result = round(float(input.get())/1.609,2)
    result_label["text"] = f"{result}"

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=1)
miles_label.config(padx=10,pady=10)

km_label = Label(text="Km")
km_label.grid(column=2,row=0)
km_label.config(padx=10,pady=10)

text_label = Label(text="is equal to")
text_label.grid(column=0,row=1)
text_label.config(padx=10,pady=10)

result_label = Label()
result_label.grid(column=1,row=1)
result_label.config(padx=10,pady=10)

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)
button.config(padx=10,pady=10)

input = Entry(width=10)
input.grid(column=1,row=0)


window.mainloop()