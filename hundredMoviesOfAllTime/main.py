from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(page.content, "html.parser")

articles = soup.findAll("section", class_="gallery__content-item")
movies = []

for article in articles:
    movie = {}
    title = article.find("h3", class_="title").getText()
    description = article.find("div", "descriptionWrapper")
    paragraphs = description.findAll("p")
    paragraph = paragraphs[1].text.strip()
    year = paragraph[:4]
    movie["rank"] = int(re.findall(r'\d+', title)[0])
    movie["title"] = title.split(" ", 1)[1]
    movie["year"] = year
    movies.append(movie)

sorted_movies = sorted(movies, key=lambda d: d['rank'])

print(sorted_movies)

with open("movies.txt", 'a') as movies:
    for movie in sorted_movies:
        rank = movie['rank']
        title = movie['title']
        year = movie['year']
        string = f"{rank}) {title}, {year}\n"
        movies.write(string)
