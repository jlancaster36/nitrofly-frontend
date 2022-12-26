from bs4 import BeautifulSoup
import requests
import urllib

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
    text = text[0].join(text[:-1])
    # Remove parentheticals
    text = text.split('(')[0]
    text = text.replace(' ', '-')
    print(text)
    return text


# https://api.rawg.io/docs/#operation/games_movies_read

test_endpoint('Metroid - Zero Mission (U) [!].gba')