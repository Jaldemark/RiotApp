from getwin import getwin, squaredEncodedImage, squaredImageList, rankToEmblem
from currentgame import getcurrentgamedata
from championId import champIdtoName
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import tools
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import json
import base64

###
###
### Doesnt work unless you have the correct api-key which Im not allowed to share publicly
###
###
app = dash.Dash()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app.config['suppress_callback_exceptions']=True
#def layout_function():
     #return
#image_list=squaredImageList()
app.layout = html.Div([
                 dcc.Tabs(id="tabs", children=[
                     dcc.Tab(label='Game stats',value='stat-tab', children=[
                                html.Div([
                                    html.Div([
                                        dcc.Input(id='summoner-id',placeholder='Summoner Name',value='',type='text'),
                                        html.Div(id='summoner-box-Div'),
                                        dcc.Input(id='champion-id',placeholder='Champion Name',value='',type='text'),
                                        html.Div(id='champion-box-Div'),
                                        html.Button(id='submit-button', n_clicks=0, children='Submit'),
                                        html.Div(id='submit-box-Div'),
                                        html.Div(id='dataframe',style={'display': 'none'})
                                        ]),
                                        html.Div([
                                            #TODO update this part
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='vision-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='d2c-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='goldearned-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='totalcs-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='turretkills-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='turretdamage-stat-id')
                                            ]),
                                            html.Div([
                                                html.H3(),
                                                dcc.Graph(id='gameduration-stat-id')
                                            ])
                                        ],style={'columnCount': 7})
                                    ])
                     ]),
                     dcc.Tab(label ='live game',value='livegame-tab',children=[
                        html.Div([
                            dcc.Input(id='summoner-id2',placeholder='Summoner Name',value='',type='text'),
                            html.Div(id='summoner-box-Div2'),
                            html.Button(id='submit-button2', children='Submit'),
                            html.Div(id='submit-box-Div2'),
                            html.Div(id='currentGameData',style={'display': 'none'}),
                            html.Div(id='currentGame')

                            ]),
                     ])
                 ]),
            html.Div(id='tab-content')
            ])

#app.layout = layout_function()
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
@app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])
def update_image_src(value,):
    return static_image_route + value
@app.callback(Output('dataframe','children'),
             [Input('submit-button','n_clicks')],
             [State('summoner-id','value'),
             State('champion-id','value')])
def update_df(n_clicks,summoner_id_name,champion_id_name):
    if n_clicks != 0:
        list = getwin(str(summoner_id_name),str(champion_id_name))
        return json.dumps(list)

@app.callback(Output('currentGameData','children'),
             [Input('submit-button2','n_clicks')],
             [State('summoner-id2','value')])
def currentGameData(n_clicks,summoner_id2_name):
    temp = getcurrentgamedata(summoner_id2_name)
    return json.dumps(temp)

@app.callback(Output('currentGame','children'),
             [Input('currentGameData','children')])
def update_currentgame(jsonified_data):

    temp = json.loads(str(jsonified_data))
    return html.Div(children=[
        #    html.H3('Live game'),
            html.Div(children=[
                html.Div([
                    html.Div('Blue team'),
                    html.Div(children=[
                                    html.Details([
                                        html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][0])),
                                                            style={
                                                                'height' :'4%',
                                                                'width' : '4%',
                                                                'display':'inline-block'
                                                                }),
                                                    html.Img(src=rankToEmblem(temp[0][0][0]['tier']),
                                                            style={
                                                            'height' :'4%',
                                                            'width' : '4%',
                                                            'display':'inline-block'}),
                                                    html.Div(temp[0][0][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                        html.Div(' Rank: ' + temp[0][0][0]['tier'].lower().title() +' '+ temp[0][0][0]['rank']),
                                        html.Div(' ranked stats: ' + str(temp[0][0][0]['wins'])+' wins and '+  str(temp[0][0][0]['losses']) + ' losses. ')
                                    ],style={'display':'inline-block'})
                                    ]),#player0
                    html.Div(children=[
                                html.Details([
                                    html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][1])),
                                                        style={
                                                            'height' :'4%',
                                                            'width' : '4%',
                                                            'display':'inline-block'
                                                            }),
                                                html.Img(src=rankToEmblem(temp[0][1][0]['tier']),
                                                        style={
                                                        'height' :'4%',
                                                        'width' : '4%',
                                                        'display':'inline-block'}),
                                                html.Div(temp[0][1][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                    html.Div(' Rank: ' + temp[0][1][0]['tier'].lower().title() +' '+ temp[0][1][0]['rank']),
                                    html.Div(' ranked stats: ' + str(temp[0][1][0]['wins'])+' wins and '+  str(temp[0][1][0]['losses']) + ' losses. ')
                                ],style={'display':'inline-block'})
                                ]),#player1
                    html.Div(children=[
                                    html.Details([
                                        html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][2])),
                                                            style={
                                                                'height' :'4%',
                                                                'width' : '4%',
                                                                'display':'inline-block'
                                                                }),
                                                    html.Img(src=rankToEmblem(temp[0][2][0]['tier']),
                                                            style={
                                                            'height' :'4%',
                                                            'width' : '4%',
                                                            'display':'inline-block'}),
                                                    html.Div(temp[0][2][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                        html.Div(' Rank: ' + temp[0][2][0]['tier'].lower().title() +' '+ temp[0][2][0]['rank']),
                                        html.Div(' ranked stats: ' + str(temp[0][2][0]['wins'])+' wins and '+  str(temp[0][2][0]['losses']) + ' losses. ')
                                    ],style={'display':'inline-block'})
                                ]),#player2
                    html.Div(children=[
                                html.Details([
                                    html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][3])),
                                                        style={
                                                            'height' :'4%',
                                                            'width' : '4%',
                                                            'display':'inline-block'
                                                            }),
                                                html.Img(src=rankToEmblem(temp[0][3][0]['tier']),
                                                        style={
                                                        'height' :'4%',
                                                        'width' : '4%',
                                                        'display':'inline-block'}),
                                                html.Div(temp[0][3][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                    html.Div(' Rank: ' + temp[0][3][0]['tier'].lower().title() +' '+ temp[0][3][0]['rank']),
                                    html.Div(' ranked stats: ' + str(temp[0][3][0]['wins'])+' wins and '+  str(temp[0][3][0]['losses']) + ' losses. ')
                                ],style={'display':'inline-block'})
                                ]),#player3
                    html.Div(children=[
                                    html.Details([
                                        html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][4])),
                                                            style={
                                                                'height' :'4%',
                                                                'width' : '4%',
                                                                'display':'inline-block'
                                                                }),
                                                    html.Img(src=rankToEmblem(temp[0][4][0]['tier']),
                                                            style={
                                                            'height' :'4%',
                                                            'width' : '4%',
                                                            'display':'inline-block'}),
                                                    html.Div(temp[0][4][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                        html.Div(' Rank: ' + temp[0][4][0]['tier'].lower().title() +' '+ temp[0][4][0]['rank']),
                                        html.Div(' ranked stats: ' + str(temp[0][4][0]['wins'])+' wins and '+  str(temp[0][4][0]['losses']) + ' losses. ')
                                    ],style={'display':'inline-block'})
                                ]),#player4
                    html.Div([
                                    html.Div('Bans:',style={'display':'inline-block'}),
                                        html.Img(src=squaredEncodedImage(champIdtoName(temp[2][0][0])),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display': 'inline-block'
                                        }),
                                        html.Img(src=squaredEncodedImage(champIdtoName(temp[2][0][1])),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display': 'inline-block'
                                        }),
                                        html.Img(src=squaredEncodedImage(champIdtoName(temp[2][0][2])),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display': 'inline-block'
                                        }),
                                        html.Img(src=squaredEncodedImage(champIdtoName(temp[2][0][3])),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display': 'inline-block'
                                        }),
                                        html.Img(src=squaredEncodedImage(champIdtoName(temp[2][0][4])),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display': 'inline-block'
                                        })
                                        ]),#bans
                ],style={'display': 'inline-block'}),
            ],style={'display': 'inline-block'}),
            html.Div(children=[
                html.Div([
                    html.Div('Red team'),
                    html.Div(children=[
                        html.Details([
                            html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][5])),
                                                style={
                                                    'height' :'4%',
                                                    'width' : '4%',
                                                    'display':'inline-block'
                                                    }),
                                        html.Img(src=rankToEmblem(temp[0][5][0]['tier']),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display':'inline-block'}),
                                        html.Div(temp[0][5][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                            html.Div(' Rank: ' + temp[0][5][0]['tier'].lower().title() +' '+ temp[0][5][0]['rank']),
                            html.Div(' ranked stats: ' + str(temp[0][5][0]['wins'])+' wins and '+  str(temp[0][5][0]['losses']) + ' losses. ')
                        ],style={'display':'inline-block'})
                        ]),#player5
                    html.Div(children=[
                            html.Details([
                                html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][6])),
                                                    style={
                                                        'height' :'4%',
                                                        'width' : '4%',
                                                        'display':'inline-block'
                                                        }),
                                            html.Img(src=rankToEmblem(temp[0][6][0]['tier']),
                                                    style={
                                                    'height' :'4%',
                                                    'width' : '4%',
                                                    'display':'inline-block'}),
                                            html.Div(temp[0][6][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                html.Div(' Rank: ' + temp[0][6][0]['tier'].lower().title() +' '+ temp[0][6][0]['rank']),
                                html.Div(' ranked stats: ' + str(temp[0][6][0]['wins'])+' wins and '+  str(temp[0][6][0]['losses']) + ' losses. ')
                            ],style={'display':'inline-block'})]),#player6
                    html.Div(children=[
                            html.Details([
                                html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][7])),
                                                    style={
                                                        'height' :'4%',
                                                        'width' : '4%',
                                                        'display':'inline-block'
                                                        }),
                                            html.Img(src=rankToEmblem(temp[0][7][0]['tier']),
                                                    style={
                                                    'height' :'4%',
                                                    'width' : '4%',
                                                    'display':'inline-block'}),
                                            html.Div(temp[0][7][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                html.Div(' Rank: ' + temp[0][7][0]['tier'].lower().title() +' '+ temp[0][7][0]['rank']),
                                html.Div(' ranked stats: ' + str(temp[0][7][0]['wins'])+' wins and '+  str(temp[0][7][0]['losses']) + ' losses. ')
                            ],style={'display':'inline-block'})
                        ]),#player7
                    html.Div(children=[
                            html.Details([
                                html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][8])),
                                                    style={
                                                        'height' :'4%',
                                                        'width' : '4%',
                                                        'display':'inline-block'
                                                        }),
                                            html.Img(src=rankToEmblem(temp[0][8][0]['tier']),
                                                    style={
                                                    'height' :'4%',
                                                    'width' : '4%',
                                                    'display':'inline-block'}),
                                            html.Div(temp[0][8][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                                html.Div(' Rank: ' + temp[0][8][0]['tier'].lower().title() +' '+ temp[0][8][0]['rank']),
                                html.Div(' ranked stats: ' + str(temp[0][8][0]['wins'])+' wins and '+  str(temp[0][8][0]['losses']) + ' losses. ')
                            ],style={'display':'inline-block'})
                        ]),#player8
                    html.Div(children=[
                        html.Details([
                            html.Summary(html.Div([html.Img(src=squaredEncodedImage(champIdtoName(temp[1][9])),
                                                style={
                                                    'height' :'4%',
                                                    'width' : '4%',
                                                    'display':'inline-block'
                                                    }),
                                        html.Img(src=rankToEmblem(temp[0][9][0]['tier']),
                                                style={
                                                'height' :'4%',
                                                'width' : '4%',
                                                'display':'inline-block'}),
                                        html.Div(temp[0][9][0]['summonerName'],style={'display':'inline-block'})],style={'display':'inline-block'})),
                            html.Div(' Rank: ' + temp[0][9][0]['tier'].lower().title() +' '+ temp[0][9][0]['rank']),
                            html.Div(' ranked stats: ' + str(temp[0][9][0]['wins'])+' wins and '+  str(temp[0][9][0]['losses']) + ' losses. ')
                        ],style={'display':'inline-block'})
                                ]),#player9
                    html.Div([
                        html.Div('Bans:',style={'display':'inline-block'}),
                            html.Img(src=squaredEncodedImage(champIdtoName(temp[2][1][0])),
                                    style={
                                    'height' :'4%',
                                    'width' : '4%',
                                    'position' : 'relative',
                                    'padding-top' : 0,
                                    'padding-right' : 0,
                                    'display': 'inline-block'
                            }),
                            html.Img(src=squaredEncodedImage(champIdtoName(temp[2][1][1])),
                                    style={
                                    'height' :'4%',
                                    'width' : '4%',
                                    'position' : 'relative',
                                    'padding-top' : 0,
                                    'padding-right' : 0,
                                    'display': 'inline-block'
                            }),
                            html.Img(src=squaredEncodedImage(champIdtoName(temp[2][1][2])),
                                    style={
                                    'height' :'4%',
                                    'width' : '4%',
                                    'position' : 'relative',
                                    'padding-top' : 0,
                                    'padding-right' : 0,
                                    'display': 'inline-block'
                            }),
                            html.Img(src=squaredEncodedImage(champIdtoName(temp[2][1][3])),
                                    style={
                                    'height' :'4%',
                                    'width' : '4%',
                                    'position' : 'relative',
                                    'padding-top' : 0,
                                    'padding-right' : 0,
                                    'display': 'inline-block'
                            }),
                            html.Img(src=squaredEncodedImage(champIdtoName(temp[2][1][4])),
                                    style={
                                    'height' :'4%',
                                    'width' : '4%',
                                    'position' : 'relative',
                                    'padding-top' : 0,
                                    'padding-right' : 0,
                                    'display': 'inline-block'
                            })
                            ])#bans
                ],style={'display': 'inline-block'}),
            ],style={'display': 'inline-block'})
    ])


@app.callback(Output('vision-stat-id','figure'),
             [Input('dataframe','children')])
def update_visionscore_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['visionscore'],
                            y=[list[3][0]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['visionscore'],
                            y=[list[2][0]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('d2c-stat-id','figure'),
             [Input('dataframe','children')])
def update_d2c_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['Total d2c'],
                            y=[list[3][1]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['Total d2c'],
                            y=[list[2][1]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('goldearned-stat-id','figure'),
             [Input('dataframe','children')])
def update_goldearned_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['Gold earned'],
                            y=[list[3][2]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['Gold earned'],
                            y=[list[2][2]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('totalcs-stat-id','figure'),
             [Input('dataframe','children')])
def update_totalcs_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['total cs'],
                            y=[list[3][3]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['total cs'],
                            y=[list[2][3]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('turretkills-stat-id','figure'),
             [Input('dataframe','children')])
def update_turretkills_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['Turret kills'],
                            y=[list[3][4]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['Turret kills'],
                                    y=[list[2][4]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('turretdamage-stat-id','figure'),
             [Input('dataframe','children')])
def update_turretdamage_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['Turret damage'],
                            y=[list[3][5]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['Turret damage'],
                            y=[list[2][5]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(
                        autosize=True,
                         width=350,
                         height=500
                        )
    }
@app.callback(Output('gameduration-stat-id','figure'),
             [Input('dataframe','children')])
def update_gameduration_Div(jsonified_data):
    list = json.loads(str(jsonified_data))
    return {
            'data':[go.Bar(x=['Game duration'],
                            y=[list[3][6]],
                            name='latest game',
                            marker=dict(
                                    color='rgb(26, 118, 255)')
                    ),
                    go.Bar(x=['Game duration'],
                            y=[list[2][6]],
                            name='average',
                            marker=dict(
                                    color='rgb(55, 83, 109)')
                    )],
            'layout':go.Layout(

                         width=350,
                         height=500
                        )
    }


if __name__ == '__main__':
        app.run_server()
