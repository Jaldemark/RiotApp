from getwin import getwin
from currentgame import getcurrentgamedata


mode = input('winrate or livegame?')
if mode == 'winrate':
    account= input('Account name: ')
    champ = input("Champion: ")
    list = getwin(account, champ)
    print('Winrate: ',list[0], account, 'on', champ)
    print(list[1][0],list[1][1],list[1][2])

elif mode == 'livegame':
    account= input('Account name: ')
    getcurrentgamedata(account)
