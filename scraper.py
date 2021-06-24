import urllib.request
from pytube import YouTube
import re 


def get_link(query, baselink="https://www.youtube.com/results?search_query="):
    returner = []
    html = urllib.request.urlopen(baselink + query.replace(' ', '+'))
    links = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for link in links[:3]:
        url = (f'https://www.youtube.com/watch?v={link}')
        yt = YouTube(url)
        returner.append([url, yt.length, yt.title])
    return returner


def get_link_one(query, baselink="https://www.youtube.com/results?search_query="):
    returner = []
    html = urllib.request.urlopen(baselink + query.replace(' ', '+'))
    links = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for link in links[:1]:
        url = (f'https://www.youtube.com/watch?v={link}')
        yt = YouTube(url)
        returner.append([url, yt.length, yt.title])
    return returner