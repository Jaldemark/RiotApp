
#Make sure the argument is from match/v4/matches
#match.json()['participants'][getParId(account,match)-1]['stats']
def getkda(match):
    tassist = match['assists']
    tdeath  = match['deaths']
    tkill   = match['kills']
    return [tkill,tdeath,tassist]
