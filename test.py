import json
from championId import ChNameToId
from championId import champIdtoName
from api import apikey
from riotwatcher import RiotWatcher, ApiError

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
watcher = RiotWatcher(apikey())

my_region = 'euw1'
version = watcher.data_dragon.versions_for_region(my_region)
me = watcher.summoner.by_name(my_region, 'Jaldemark')
ddragon = watcher.data_dragon.champions('9.3.1', locale=None)

image_directory = '9.3.1/img/champion'
list_of_images=[]
for img in os.listdir(image_directory):
    list_of_images.append(img)

print(ddragon['data']['Zyra']['image']['sprite'])

img=mpimg.imread('9.3.1/img/champion/'+list_of_images[123])
imgplot = plt.imshow(img)
plt.show()

print(ddragon['data']['Zyra']['image']['sprite'])
