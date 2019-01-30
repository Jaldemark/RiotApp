from getwin import getwin


#TODO add player name/id as argument


account= input('Account name: ')
champ = input("Champion: ")
list = getwin(account, champ)
print('Winrate: ',list[0], account, 'on', champ)
print(list[1][0],list[1][1],list[1][2])
