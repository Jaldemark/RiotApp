import requests
from championId import ChNameToId
from seasons import seasonId
from api import apikey
from queueId import queueId
def getwin(account, champ):

    URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey()
    response = requests.get(URL)
    rj = response.json()
    #AccountId visar error ibland av oklar anledning
    URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion="+str(ChNameToId(champ))+"&api_key="+apikey()
    match2 = requests.get(URL2)
    print(match2.json())
    wincounter =0
    fittcounters =0
    count = 0
    fitterror = 0
    while(count<match2.json()['endIndex']):
        #try:
            gameId = match2.json()['matches'][count]['gameId']
            season = match2.json()['matches'][count]['season']
            queuetype = match2.json()['matches'][count]['queue']
            URL =  "https://euw1.api.riotgames.com/lol/match/v3/matches/"+str(gameId)+"?api_key="+apikey()
            match = requests.get(URL)
            if queuetype == 420:
                print(match.json())
                if match.json()['teams'][0]['win'] == 'Win':
                    wincounter = wincounter + 1
                fittcounters = fittcounters+1
                print('Game: ',fittcounters,'Win counter: ',wincounter, seasonId(season), 'queue: ', queueId(queuetype))
            count = count + 1
            #print('Game: ',count,'Win counter: ',wincounter, seasonId(season), 'queue: ', queueId(queuetype))

        #except:
              # print('Fitt error')
              # count = count+1
               #fitterror = fitterror+1

    return wincounter/fittcounters
