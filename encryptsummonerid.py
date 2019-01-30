from api import apikey
import requests
def encryptedSummonerId(account, mode):
    url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey()
    response = requests.get(url)
    if mode == 1:
        return response.json()['id']
    elif mode == 2:
        return response.json()['accountId']
