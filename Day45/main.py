from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

top100_webpage = response.text

soup = BeautifulSoup(top100_webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")

top_movies = [movie.text for movie in movies]
top_movies.reverse()


with open("Day45/top100.txt", "w") as file:
    for movie in top_movies:
        if movie == "59) E.T. â\x80\x93 The Extra Terrestrial":
            file.write("59) E.T. - The Extra Terrestrial\n")
        else:
            file.write(f"{movie}\n")