from getwin import getwin
from currentgame import getcurrentgamedata
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import tools

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
    xvalues = []
    yvalues = [[],[],[]]
    count = 0
    for item in list[4]:
        for x in list[4][item]:
            xvalues.append(x)
        for y in list[4][item].values():
            yvalues[count].append(y)
        count +=1

    trace1 = go.Scatter(x=xvalues,y=yvalues[0],
                       mode='lines+markers', name='Creep per min')
    trace2 = go.Scatter(x=xvalues,y=yvalues[1],
                       mode='lines+markers', name='Xp per min')
    trace3 = go.Scatter(x=xvalues,y=yvalues[2],
                       mode='lines+markers', name='Gold per min')

    fig = tools.make_subplots(rows=1, cols=3, subplot_titles=('Creep', 'Xp', 'Gold'))
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 1, 3)
    fig['layout'].update(height=600, width=1200, title='Delta stats')
    pyo.plot(fig)

elif mode == 'livegame':
    account= input('Account name: ')
    getcurrentgamedata(account)
