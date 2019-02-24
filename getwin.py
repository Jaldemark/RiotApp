import requests
from championId import ChNameToId
from seasons import seasonId
from api import apikey
from queueId import queueId
from collections import Counter
from itertools import chain
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import base64
#Doesnt work properly if the player changed name
def getParId(account,match):
    for key in match.json()['participantIdentities']:
        if key['player']['summonerName']==account:
            return key['participantId']
    return 11
def getwin(account, champ):
    try:
        wincounter =0
        validcounter =0
        count = 0
        kda =[0]*3
        statlist = [0]*7
        latestgame = True
        deltalist = []*4
        #spaghett
        creeplist = {'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0}
        explist = {'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0}
        goldlist = {'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0}
        deltalist = {'creeplist':creeplist,'explist':explist,'goldlist':goldlist}
        URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+account+"?api_key="+apikey()
        response = requests.get(URL)
        rj = response.json()
        URL2 = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+rj['accountId']+"?champion="+str(ChNameToId(champ))+"&api_key="+apikey()
        match2 = requests.get(URL2)
        index = match2.json()['endIndex']
        latestgame = True

        while(count<(match2.json()['endIndex']-1 or count<75)):
            gameId = match2.json()['matches'][count]['gameId']
            season = match2.json()['matches'][count]['season']
            queuetype = match2.json()['matches'][count]['queue']
            URL =  "https://euw1.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key="+apikey()
            match = requests.get(URL)
            timestamp = {'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0}
            if getParId(account,match) != 11:
                if latestgame:
                    latestgamestat = getStats(match,getParId(account,match)-1)
                    latestgame = False
                temp = getDeltas(match,getParId(account,match)-1)
                #all have the same length so doesnt matter which you use but can propably be done in a better way
                for k in temp['creepsPerMinDeltas']:
                    if k == '30-end':
                        s = '30-40'
                        deltalist['creeplist'][s]  = (deltalist['creeplist'][s]*timestamp[s]+temp['creepsPerMinDeltas'][k])/(timestamp[s]+1)
                        deltalist['explist'][s]      = (deltalist['explist'][s]*timestamp[s]+temp['xpPerMinDeltas'][k])/(timestamp[s]+1)
                        deltalist['goldlist'][s]    = (deltalist['goldlist'][s]*timestamp[s]+temp['goldPerMinDeltas'][k])/(timestamp[s]+1)
                    if 'end' not in k:
                        timestamp[k] +=1
                        deltalist['creeplist'][k]  = (deltalist['creeplist'][k]*timestamp[k]+temp['creepsPerMinDeltas'][k])/(timestamp[k]+1)
                        deltalist['explist'][k]      = (deltalist['explist'][k]*timestamp[k]+temp['xpPerMinDeltas'][k])/(timestamp[k]+1)
                        deltalist['goldlist'][k]    = (deltalist['goldlist'][k]*timestamp[k]+temp['goldPerMinDeltas'][k])/(timestamp[k]+1)
                lists_of_lists = [kda, getkda(match.json()['participants'][getParId(account,match)-1]['stats'])]
                kda = [sum(x) for x in zip(*lists_of_lists)]

                lists_of_lists = [statlist, getStats(match,getParId(account,match)-1)]
                statlist = [sum(x) for x in zip(*lists_of_lists)]

                if getParId(account,match) != 11 and match.json()['participants'][getParId(account,match)-1]['stats']['win'] == True:
                    wincounter += 1
                validcounter += 1
                kdastr = 'K/D/A: '+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[0])+'/'+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[1])+'/'+str(getkda(match.json()['participants'][getParId(account,match)-1]['stats'])[2])
                print('Game: ',validcounter,'Win counter: ',wincounter, seasonId(season), 'queue: ', queueId(queuetype), kdastr)
            count += 1


    except Exception as e:
           print(e)
           count = count+1

        #except Exception as e:
               #print(e)
               #count = count+1
               #validcounter +=1
    kda[:] = [x/validcounter for x in kda]
    statlist[:] = [x/validcounter for x in statlist]
    return [wincounter/validcounter, kda, statlist, latestgamestat,deltalist,validcounter]


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
    return {'creepsPerMinDeltas':temp['creepsPerMinDeltas'],'xpPerMinDeltas':temp['xpPerMinDeltas'],'goldPerMinDeltas':temp['goldPerMinDeltas']}

def squaredEncodedImage(champion):
    image_directory = 'assets/9.3.1/img/champion/'
    # '9.3.1/img/champion'+champion
    list_of_images=[]
    dic={" ":"","'":"",".":""}
    for i, j in dic.items():
        champion = champion.replace(i, j)
    if champion == 'Wukong':
        champion = 'MonkeyKing'
    image_filename = image_directory+champion+'.png'
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    trendImage = 'data:image/png;base64,{}'.format(encoded_image.decode())
    return trendImage

def squaredImageList():
    image_directory = 'assets/9.3.1/img/champion'
    list_of_images=[]
    for img in os.listdir(image_directory):
        image_filename =image_directory +'/'+ img
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        list_of_images.append(encoded_image)
    return list_of_images

def rankToEmblem(the_rank):
    temp = the_rank.lower().title()
    image_directory = 'emblem_rank/Emblem_'+temp+'.png'
    encoded_image = base64.b64encode(open(image_directory, 'rb').read())
    trendImage = 'data:image/png;base64,{}'.format(encoded_image.decode())
    return trendImage
