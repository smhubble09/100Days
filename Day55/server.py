from random import randint
from flask import Flask
app = Flask(__name__)

random_num = randint(0,9)

@app.route('/')
def home():
    return '<h1>Guess a nmber between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Numbers">'

@app.route('/<int:number>')
def number_guess(number):
    if number > random_num:
        return '<h1 style="color=red">Too high, try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Too High">'
    elif number < random_num:
        return '<h1 style="color=purple">Too low, try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Too Low">'
    else:
        return '<h1 style="color=green">You found me!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct">'

if __name__ == "__main__":
    app.run(debug=True)