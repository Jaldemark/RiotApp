import requests
from championId import ChNameToId
from seasons import seasonId
from api import apikey
from queueId import queueId
from kda import getkda

def getParId(account,match):
    for key in match.json()['participantIdentities']:
        if key['player']['summonerName']==account:
            return key['participantId']
    return 11
def getwin(account, champ):

    URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey()
    response = requests.get(URL)
    rj = response.json()
    #AccountId visar error ibland av oklar anledning
    URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion="+str(ChNameToId(champ))+"&api_key="+apikey()
    match2 = requests.get(URL2)
    wincounter =0
    fittcounters =0
    count = 0
    kda =[0,0,0]
    index = match2.json()['endIndex']
    print(index)
    while(count<(match2.json()['endIndex']-1)):
        try:
            gameId = match2.json()['matches'][count]['gameId']
            season = match2.json()['matches'][count]['season']
            queuetype = match2.json()['matches'][count]['queue']

            URL =  "https://euw1.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key="+apikey()
            match = requests.get(URL)

            #if queuetype == 420:

            if getParId(account,match) != 11:
                noob = getkda(match.json()['participants'][getParId(account,match)-1]['stats'])
                lists_of_lists = [kda, getkda(match.json()['participants'][getParId(account,match)-1]['stats'])]
                kda = [sum(x) for x in zip(*lists_of_lists)]
                if getParId(account,match) != 11 and match.json()['participants'][getParId(account,match)-1]['stats']['win'] == True:
                    wincounter = wincounter + 1
                fittcounters = fittcounters+1

                noobstr = 'K/D/A: '+str(kda[0])+'/'+str(kda[1])+'/'+str(kda[2])
                print('Game: ',fittcounters,'Win counter: ',wincounter, seasonId(season), 'queue: ', queueId(queuetype), noob)
            count = count + 1

        except Exception as e:
               print(e)
               count = count+1

    kda[0]=kda[0]/fittcounters
    kda[1]=kda[1]/fittcounters
    kda[2]=kda[2]/fittcounters
    return [wincounter/fittcounters, kda]
