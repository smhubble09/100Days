from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    curr_year = datetime.today().year
    return render_template('index.html', year=curr_year)

@app.route('/guess/<some_name>')
def guess(some_name):
    age_response = requests.get(f"https://api.agify.io/?name={some_name}")
    guessed_age = age_response.json()["age"]
    gender_response = requests.get(f"https://api.genderize.io/?name={some_name}")
    guessed_gender = gender_response.json()["gender"]
    return render_template('guess.html', name=some_name.title(), gender=guessed_gender, age=guessed_age)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/4af156202f984d3464c3"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)