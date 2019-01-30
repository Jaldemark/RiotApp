    import requests

URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Jaldemark?api_key=RGAPI-fda09105-57a6-409c-9898-c6b0206336e5"
response = requests.get(URL)
#print(response['accountId'])

rj = response.json()
print(rj)
URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion=13&api_key=RGAPI-fda09105-57a6-409c-9898-c6b0206336e5"
match = requests.get(URL2)


def getWin(matchID):
    URL =  "https://euw1.api.riotgames.com/lol/match/v3/matches/"+str(matchID)+"?api_key=RGAPI-fda09105-57a6-409c-9898-c6b0206336e5"
    match = requests.get(URL)

    for key in match.json():
        print(key['teams']['win'])


print(match.json())
matchID = match.json()['matches'][2]['gameId']
getWin(matchID)
print(matchID)
