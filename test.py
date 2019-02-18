import json
from championId import ChNameToId
from championId import champIdtoName
from api import apikey
from riotwatcher import RiotWatcher, ApiError

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import plotly.offline as pyo
import plotly.plotly as py
import plotly.graph_objs as go

watcher = RiotWatcher(apikey())

my_region = 'euw1'
version = watcher.data_dragon.versions_for_region(my_region)
me = watcher.summoner.by_name(my_region, 'Jaldemark')
ddragon = watcher.data_dragon.champions('9.3.1', locale=None)


#img=mpimg.imread(list_of_images[123])
#imgplot = plt.imshow(img)
#plt.show()
