import requests
import json
from championId import ChNameToId
from seasons import seasonId
apikey = "RGAPI-03ded2e1-f816-48cb-8a05-31e858cd703f"


#TODO add player name/id as argument
def getParId(match):
    for key in match.json()['participantIdentities']:
        if key['player']['summonerName']=='Jaldemark':
            return key['participantId']
def getWin(account, champ):

    URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey
    response = requests.get(URL)
    rj = response.json()

    URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion="+str(ChNameToId(champ))+"&api_key="+apikey
    match2 = requests.get(URL2)
    print(match2.json()['endIndex'])
    wincounter =0
    count = 0
    fitterror = 0
    while(count<match2.json()['endIndex']):
        try:
            gameId = match2.json()['matches'][count]['gameId']
            season = match2.json()['matches'][count]['season']
            print('--------------------------------------------------------------------------------------------')
            URL =  "https://euw1.api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+apikey
            match = requests.get(URL)
            if match.json()['teams'][0]['win'] == 'Win':
                wincounter = wincounter + 1
            print('Game: ',count,'Win counter: ',wincounter, seasonId(season))
            count = count + 1

        except:
               print('Fitt error')
               count = count+1
               fitterror = fitterror+1

    return wincounter/(match2.json()['endIndex']-fitterror)
account= input('Account name: ')
champ = input("Champion: ")
print('Winrate: ',getWin(account, champ), account, 'on', champ)
