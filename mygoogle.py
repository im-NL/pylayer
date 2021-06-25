from googleapiclient.discovery import build 
from datetime import datetime

api_key = 'AIzaSyDZviY4Ef4ND_gSTIEFDBkClueiiq5ILQo'
youtube = build('youtube', 'v3', developerKey=api_key)

def get_link(query):
    links = []
    req = youtube.search().list(q=query, type='video', part='snippet')
    results = req.execute()
#        links.append('https://youtube.com/watch?v=' + result['id']['videoId'])
    for i in range(5):
        templist = []
        templist.append('Title --> ' + results['items'][i]['snippet']['title'])
        templist.append('https://youtube.com/watch?v=' + results['items'][i]['id']['videoId'])
        links.append(templist)
    return links

def get_link_one(query):
    req = youtube.search().list(q=query, type='video', part='snippet')
    results = req.execute()
    link = 'https://youtube.com/watch?v=' + results['items'][0]['id']['videoId']
    return link 

def song_length(url):
    req = youtube.search().list(q=url, type='video', part='snippet')
    results = req.execute()
    id = results['items'][0]['id']['videoId']
    req = youtube.videos().list(id=id, part='contentDetails')
    returned_content = req.execute()
    duration = returned_content['items'][0]['contentDetails']['duration']
    return duration     

