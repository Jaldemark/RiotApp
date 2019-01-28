import requests
import json
from championId import ChNameToId
apikey = "RGAPI-03ded2e1-f816-48cb-8a05-31e858cd703f"




URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Jaldemark?api_key="+apikey
response = requests.get(URL)
rj = response.json()

URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion=13&api_key="+apikey
match2 = requests.get(URL2)

print(match2.json())
