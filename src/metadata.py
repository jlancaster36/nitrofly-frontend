from bs4 import BeautifulSoup
import requests
import os
import urllib
from igdb.wrapper import IGDBWrapper
import json
from time import sleep
import pandas as pd


client_secret = os.environ.get('client_secret', '6ot1o0dhe99fy8z47mjz2cxwarge7h')
client_id = os.environ.get('client_id', 'hpzcuu7ynamdf4xuv99ogsjbxulfs9')




def getIGDBToken():
    grant_type = 'client_credentials'
    url = f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type={grant_type}'
    # print(url)
    auth = requests.post(url)
    # print(auth)
    token = auth.json()["access_token"]
    return token

wrapper = IGDBWrapper(client_id, getIGDBToken())

def getMetadata():
    print('')

def get_media(title):
    pass

def setup_text(title):
    pass

def setup_other(title):
    pass


def test_endpoint(filename: str):
    search = filter_title(filename)
    base =  f"https://api.rawg.io/api/games{search}/movies"
    resp = requests.get(base)
    print(resp)

def scrape_igdb(filename: str):
    game = filter_title(filename)
    r = requests.get(f"https://www.igdb.com/games/{game}")
    soup = BeautifulSoup(r.content, 'html.parser')
 
    # List of all video tag
    video_tags = soup.findAll('video')
    print("Total ", len(video_tags), "videos found")
 
    if len(video_tags) != 0:
        for video_tag in video_tags:
            video_url = video_tag.find("a")['href']
            print(video_url)
    else:
        print("no videos found")


def filter_title(title: str):
    # Remove file extension
    text = title.split('.')[:-1]
    text = "".join(text)
    text = text.split('(')[0]

    print(text)
    return text

def IGDBSearch(name):
    token = getIGDBToken()
    # print(token)
    #TODO: Search by platform for ports
    search = filter_title(name)
    byte_array = wrapper.api_request(
            'search',
            f'search "{search}"; fields game, name; offset 0;'
          )
    sleep(1)
    resp = byte_array.decode("utf-8");
    data = json.loads(resp)
    # s = json.dumps(data, indent=4, sort_keys=True)
    print(type(data))
    try:
        game_id = data[0]["game"]
        game_name = data[0]["name"]
    except:
        print("No metadata found")
        game_name = name
        return None
    
    return game_id
    
def getGameData(game_id):
    #TODO: Get all game data from scanned directory in 1 query
    byte_array = wrapper.api_request(
            'games',
            f'fields cover,artworks,name,videos,summary; where id = {game_id};'
          )
    resp = byte_array.decode("utf-8")
    data = json.loads(resp)
    print (data)

def getGameVideo(platform, name):
    #TODO: Download screen scraper gamelists and use as lookup table for game ID
    url = 'https://www.screenscraper.fr/gameinfos.php?plateforme=13&gameid=4798'
# https://api.rawg.io/docs/#operation/games_movies_read

# For a possible webscrape solutions:
    # https://www.igdb.com/games/super-metroid
        # API Link: https://api-docs.igdb.com/#about
    # https://www.gamesdatabase.org/all_videos
    # each gamepage has boxart, support, and video


# test_endpoint('Metroid - Zero Mission (U) [!].gba')\
id = IGDBSearch('Mario Superstar Baseball (USA).iso')
getGameData(id)