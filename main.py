from getwin import getwin


#TODO add player name/id as argument
def getParId(account):
    for key in match.json()['participantIdentities']:
        if key['player']['summonerName']==account:
            return key['participantId']

account= input('Account name: ')
champ = input("Champion: ")
print('fitta')
print('Winrate: ',getwin(account, champ), account, 'on', champ)
