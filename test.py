import json
from championId import ChNameToId
from championId import champIdtoName
#from pprint import pprint

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':5,'b':1,'c':7}
print(type(dict1['a']))
dict1['a'] = dict1['a']+dict2['a']
print(dict1['a'])
