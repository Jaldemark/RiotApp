import requests
from championId import ChNameToId
from seasons import seasonId
from api import apikey
from queueId import queueId
from collections import Counter
from itertools import chain
from collections import defaultdict

#Doesnt work properly if the player changed name
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
    kda =[0]*3
    statlist = [0]*7
    index = match2.json()['endIndex']
    latestgame = True
    deltalist = []*4
    while(count<(match2.json()['endIndex']-1 or count<75)):
    #    try:
            gameId = match2.json()['matches'][count]['gameId']
            season = match2.json()['matches'][count]['season']
            queuetype = match2.json()['matches'][count]['queue']
            URL =  "https://euw1.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key="+apikey()
            match = requests.get(URL)
            if getParId(account,match) != 11:
                if latestgame:
                    latestgamestat = getStats(match,getParId(account,match)-1)
                    latestgame = False
                    deltalist = getDeltas(match,getParId(account,match)-1)
                else:
                    temp = getDeltas(match,getParId(account,match)-1)
                    deltacount =0
                    print(deltalist)
                    newlist = []*3
                    for dicts in temp:
                        print(dicts)
                        for k in dicts:
                            print(deltalist[deltacount])
                            newlist[deltacount] = {k, deltalist[deltacount][k] + temp[deltacount][k]}
                        deltacount +=1
                    print(newlist)

                lists_of_lists = [kda, getkda(match.json()['participants'][getParId(account,match)-1]['stats'])]
                kda = [sum(x) for x in zip(*lists_of_lists)]

                lists_of_lists = [statlist, getStats(match,getParId(account,match)-1)]
                statlist = [sum(x) for x in zip(*lists_of_lists)]

                if getParId(account,match) != 11 and match.json()['participants'][getParId(account,match)-1]['stats']['win'] == True:
                    wincounter += 1
                fittcounters += 1
                kdastr = 'K/D/A: '+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[0])+'/'+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[1])+'/'+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[2])
                print('Game: ',fittcounters,'Win counter: ',wincounter, seasonId(season), 'queue: ', queueId(queuetype), kdastr)
            count += 1

        #except Exception as e:
              # print(e)
               #count = count+1
    print(statlist[0])
    kda[:] = [x/fittcounters for x in kda]
    statlist[:] = [x/fittcounters for x in statlist]
    return [wincounter/fittcounters, kda, statlist, latestgamestat, dict(c)]

def getkda(match):
    tassist = match['assists']
    tdeath  = match['deaths']
    tkill   = match['kills']
    return [tkill,tdeath,tassist]

def getStats(match,parId):
    visionscore = match.json()['participants'][parId]['stats']['visionScore']
    totalDamageDealtToChampions = match.json()['participants'][parId]['stats']['totalDamageDealtToChampions']
    goldearned = match.json()['participants'][parId]['stats']['goldEarned']
    totalminions = match.json()['participants'][parId]['stats']['totalMinionsKilled']
    turretstaken = match.json()['participants'][parId]['stats']['turretKills']
    turretdamage = match.json()['participants'][parId]['stats']['damageDealtToTurrets']
    gametime = match.json()['gameDuration']
    return [visionscore,totalDamageDealtToChampions, goldearned,totalminions,turretstaken,turretdamage,gametime]

def getDeltas(match,parId):
    temp = match.json()['participants'][parId]['timeline']
    return [temp['creepsPerMinDeltas'],temp['xpPerMinDeltas'],temp['goldPerMinDeltas']]
