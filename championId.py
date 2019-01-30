import json
def ChNameToId(name):
    config = json.loads(open('champion.json',encoding="utf8").read())
    return config['data'][name]['key']
def champIdtoName(id):
    config = json.loads(open('champion.json',encoding="utf8").read())
    for champ in config['data']:
        if config['data'][champ]['key'] == str(id):
            return champ
