import re
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# FOLLOW STEPS FROM HERE: https://developers.deezer.com/api/oauth TO HAVE ADMIN PLAYLIST PRIVILEGE

load_dotenv()
deezer_id = os.environ["DEEZER_API_ID"]
deezer_key = os.environ["DEEZER_API_KEY"]
deezer_create_playlist_url = os.environ["DEEZER_CREATE_PLAYLIST_URL"]
deezer_add_to_playlist_url = os.environ["DEEZER_ADD_TO_PLAYLIST_URL"]
deezer_search_url = os.environ["DEEZER_SEARCH_URL"]
deezer_access_token = os.environ["DEEZER_ACCESS_TOKEN"]
deezer_playlist_id = os.environ["DEEZER_PLAYLIST_ID"]

billboard_url = "https://www.billboard.com/charts/hot-100/"

desired_date = input("What billboard are you interested in? Type the date in the format YYYY-MM-DD:\n")

songs_ids = []

if re.match(r'\d{4}-\d{2}-\d{2}', desired_date):
    # ONLY FOR CREATING THE PLAYLIST THE FIRST TIME
    # parameters = {
    #     "access_token": deezer_access_token,
    #     "title": f"Billboard 100 of {desired_date}"
    # }
    # response = requests.post(url=deezer_create_playlist_url, params=parameters)
    # print(response.text)

    url = f"{billboard_url}/{desired_date}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    songs = soup.findAll("div", class_="o-chart-results-list-row-container")
    for song in songs:
        entry = {}
        title = song.select("ul li ul li h3")[0].text.strip()
        artist = song.select("ul li ul li span")[0].text.strip()
        parameters = {
            "q": title
        }
        response = requests.get(url=deezer_search_url, params=parameters)
        data = response.json()
        try:
            song_id = data["data"][0]["id"]
        except:
            print(f"{title} not found.")
        else:
            songs_ids.append(str(song_id))
    songs_list = ','.join(songs_ids)
    parameters = {
        "access_token": deezer_access_token,
        "songs": songs_list
    }
    post_tracks_url = f"{deezer_add_to_playlist_url}/{deezer_playlist_id}/tracks"
    response = requests.post(url=post_tracks_url, params=parameters)
    print(response.text)
else:
    print("Well, you cannot enter a date, you don't get the playlist MF")
