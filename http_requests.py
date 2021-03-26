import requests
import json
from bs4 import BeautifulSoup


def send_http_request(url):
    r = requests.get(url)
    try:
        print(r.json()['content'])
    except:
        print('Invalid quote resource!')


def movie_title_and_description(url):
    req = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if req:
        soup = BeautifulSoup(req.content, "html.parser")

        description = soup.find('div', {'class': "summary_text"})
        if description:
            movie_d = {"title": soup.title.text, "description": description.text.strip()}
            print(movie_d)
        else:
            print('Invalid movie page!')


user_input = "https://www.imdb.com/title/tt0080684/"
# send_http_request(user_input)
movie_title_and_description(user_input)
