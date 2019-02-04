from getwin import getwin
from currentgame import getcurrentgamedata
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

mode = input('winrate or livegame?')
if mode == 'winrate':
    account= input('Account name: ')
    champ = input("Champion: ")
    list = getwin(account, champ)
    print('Winrate: ',list[0], account, 'on', champ)
    print('Average K/D/A: ', list[1][0],list[1][1],list[1][2])
    print('Latest game stat compared to average')

    print('Latest vision score: ',list[3][0], 'Compared to average:',list[2][0])
    print('Latest total damage dealt to champions: ',list[3][1], 'Compared to average:',list[2][1])
    print('Latest Gold earned: ',list[3][2], 'Compared to average:',list[2][2])
    print('Latest total creep score: ',list[3][3], 'Compared to average:',list[2][3])
    print('Latest Turret kills: ',list[3][4], 'Compared to average:',list[2][4])
    print('Latest Turret damage: ',list[3][5], 'Compared to average:',list[2][5])
    print('Latest Game time in minutes: ',list[3][6]/60, 'Compared to average:',list[2][6]/60)
    print('Delta:', list[4]['creeplist'], list[5])
    xvalues =[]
    yvalues =[]
    for x in list[4]['creeplist']:
        xvalues.append(x)
    for y in list[4]['creeplist'].values():
        yvalues.append(y)

    print(xvalues,yvalues)
    trace = go.Scatter(x=xvalues,y=yvalues,
                       mode='lines+markers', name='lineAndMarkers')
    data = [trace]
    layout = go.Layout(title='Creep per min')

    fig = go.Figure(data,layout)
    pyo.plot(fig)
elif mode == 'livegame':
    account= input('Account name: ')
    getcurrentgamedata(account)
