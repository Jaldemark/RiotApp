import json
from championId import ChNameToId
from championId import champIdtoName
#from pprint import pprint

print(champIdtoName())
config = json.loads(open('champion.json',encoding="utf8").read())
for champ in config['data']:
    if config['data'][champ]['key'] == '119':
        print(champ)
