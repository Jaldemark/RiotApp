import requests
from api import apikey
from encryptsummonerid import encryptedSummonerId
def getcurrentgamedata(account):
    URL = "https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+str(encryptedSummonerId(account))+"?api_key="+apikey()
    response = requests.get(URL)
    print(response.json())
