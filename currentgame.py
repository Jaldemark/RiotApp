import requests
from api import apikey
from encryptsummonerid import encryptedSummonerId
from championId import champIdtoName

champlist = []
playerlist = []
#/lol/match/v4/timelines/by-match/{matchId}
def getcurrentgamedata(account):

        URL = "https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+str(encryptedSummonerId(account,1))+"?api_key="+apikey()
        response = requests.get(URL)
        match = response.json()
        url = "https://euw1.api.riotgames.com/lol/league/v4/positions/by-summoner/"+str(encryptedSummonerId(account,1))+"?api_key="+apikey()
        response = requests.get(url)
        rank = response.json()
        for player in match['participants']:
            url = "https://euw1.api.riotgames.com/lol/league/v4/positions/by-summoner/"+str(encryptedSummonerId(player['summonerName'],1))+"?api_key="+apikey()
            response = requests.get(url)
            rank= response.json()
            if len(rank)==0:
                playerlist.append([{'summonerName':player['summonerName'],'tier':'unranked','rank':'unranked','wins':'unknown','losses':'unknown'}])
            else:
                playerlist.append(rank)
        for champ in match['participants']:
            champlist.append(champ['championId'])
        gen1 = (ban['championId'] for ban in match['bannedChampions'] if ban['teamId']==100)
        gen2 = (ban['championId'] for ban in match['bannedChampions'] if ban['teamId']==200)
        print('Blue team')
        print('Player:',playerlist[0][0]['summonerName'], 'Champion:',champIdtoName(champlist[0]),'Rank:',playerlist[0][0]['tier'],playerlist[0][0]['rank'], 'ranked stats:',playerlist[0][0]['wins'],'wins and', playerlist[0][0]['losses'], 'losses.')
        print('Player:',playerlist[1][0]['summonerName'], 'Champion:',champIdtoName(champlist[1]),'Rank:',playerlist[1][0]['tier'],playerlist[1][0]['rank'], 'ranked stats:',playerlist[1][0]['wins'],'wins and', playerlist[1][0]['losses'], 'losses.')
        print('Player:',playerlist[2][0]['summonerName'], 'Champion:',champIdtoName(champlist[2]),'Rank:',playerlist[2][0]['tier'],playerlist[2][0]['rank'], 'ranked stats:',playerlist[2][0]['wins'],'wins and', playerlist[2][0]['losses'], 'losses.')
        print('Player:',playerlist[3][0]['summonerName'], 'Champion:',champIdtoName(champlist[3]),'Rank:',playerlist[3][0]['tier'],playerlist[3][0]['rank'], 'ranked stats:',playerlist[3][0]['wins'],'wins and', playerlist[3][0]['losses'], 'losses.')
        print('Player:',playerlist[4][0]['summonerName'], 'Champion:',champIdtoName(champlist[4]),'Rank:',playerlist[4][0]['tier'],playerlist[4][0]['rank'], 'ranked stats:',playerlist[4][0]['wins'],'wins and', playerlist[4][0]['losses'], 'losses.')
        print('Bans blue:',[champIdtoName(x) for x in gen1])
        print(' ')
        print('Red team')
        print('Player:',playerlist[5][0]['summonerName'], 'Champion:',champIdtoName(champlist[5]),'Rank:',playerlist[5][0]['tier'],playerlist[5][0]['rank'], 'ranked stats:',playerlist[5][0]['wins'],'wins and', playerlist[5][0]['losses'], 'losses.')
        print('Player:',playerlist[6][0]['summonerName'], 'Champion:',champIdtoName(champlist[6]),'Rank:',playerlist[6][0]['tier'],playerlist[6][0]['rank'], 'ranked stats:',playerlist[6][0]['wins'],'wins and', playerlist[6][0]['losses'], 'losses.')
        print('Player:',playerlist[7][0]['summonerName'], 'Champion:',champIdtoName(champlist[7]),'Rank:',playerlist[7][0]['tier'],playerlist[7][0]['rank'], 'ranked stats:',playerlist[7][0]['wins'],'wins and', playerlist[7][0]['losses'], 'losses.')
        print('Player:',playerlist[8][0]['summonerName'], 'Champion:',champIdtoName(champlist[8]),'Rank:',playerlist[8][0]['tier'],playerlist[8][0]['rank'], 'ranked stats:',playerlist[8][0]['wins'],'wins and', playerlist[8][0]['losses'], 'losses.')
        print('Player:',playerlist[9][0]['summonerName'], 'Champion:',champIdtoName(champlist[9]),'Rank:',playerlist[9][0]['tier'],playerlist[9][0]['rank'], 'ranked stats:',playerlist[9][0]['wins'],'wins and', playerlist[9][0]['losses'], 'losses.')
        print('Bans red: ',[champIdtoName(x) for x in gen2])
