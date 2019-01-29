import requests
import json
from championId import ChNameToId
from api import apikey

URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Jaldemark?api_key="+apikey()
response = requests.get(URL)
rj = response.json()

URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion=13&api_key="+apikey()
match2 = requests.get(URL2)
count = 0
while(count<match2.json()['endIndex']):

    game = match2.json()['matches'][count]['gameId']
    URL3 =  "https://euw1.api.riotgames.com/lol/match/v4/matches/"+str(game)+"?api_key="+apikey()
    response = requests.get(URL3)
    match = response.json()
    print(match['participants'][count]['stats'])
    print('-------------------------------------------------------------------------------------')
    count = count+1
