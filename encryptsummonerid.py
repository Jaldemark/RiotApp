from api import apikey
import requests
def encryptedSummonerId(account):
    url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey()
    response = requests.get(url)
    return response.json()['id']
