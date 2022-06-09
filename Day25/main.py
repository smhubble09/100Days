import turtle
import pandas


IMAGE = "Day25/blank_states_img.gif"
FONT = ("Courier", 7, "normal")
ALIGNMENT = "center"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)

screen.addshape(IMAGE)
turtle.shape(IMAGE)
#Get coordinates for states
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


class StateName(turtle.Turtle):
    def __init__(self,x,y,state) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)   
        self.write(f"{state}", align=ALIGNMENT, font=FONT)

data = pandas.read_csv("Day25/50_states.csv")

guessed_states = []

#Loop game while there's still states to guess
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="Name a State").title()

    if answer_state == "Exit":
        break
    for state in data.state:
        if answer_state not in guessed_states:
            if answer_state == state:
                guessed_states.append(answer_state)
                #Get data for guessed state
                state_data = data[data.state == answer_state]
                #Create a new turtle with the x & y coords of guessed state
                new_state = StateName(int(state_data.x),int(state_data.y),answer_state)

#States to learn
missed_states = []

for state in data.state:
    if state not in guessed_states:
        missed_states.append(state)

data_dict = {
    "States to Learn": missed_states
}

df = pandas.DataFrame(data_dict)

df.to_csv("Day25/states_to_learn.csv")