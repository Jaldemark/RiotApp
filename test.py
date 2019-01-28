import requests
import json
from championId import ChIDToName
apikey = "RGAPI-b42ead60-93da-4c02-b348-0931995ed92d"


#TODO add player name/id as argument
def getParId(match):
    for key in match.json()['participantIdentities']:
        if key['player']['summonerName']=='Dukoez':
            return key['participantId']
def getWin():

    URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Jaldemark?api_key="+apikey
    response = requests.get(URL)
    rj = response.json()

    URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion=58&api_key="+apikey
    match2 = requests.get(URL2)
    print(match2.json()['endIndex'])
    wincounter =0
    count = 0
    print
    while(count<match2.json()['endIndex']):
        try:
            gameId = match2.json()['matches'][count]['gameId']
            print('--------------------------------------------------------------------------------------------')
            print(match.json())
            URL =  "https://euw1.api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+apikey
            match = requests.get(URL)
            if match.json()['teams'][0]['win'] == 'Win':
                wincounter = wincounter + 1
            print('Game: ',count,'Win counter: ',wincounter)
            count = count + 1

        except:
                print('Fitt error')
                count = count+1

    return wincounter/match2.json()['endIndex']

print('Winrate: ',getWin())
