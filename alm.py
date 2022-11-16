
# sound effects from https://sound-effects.bbcrewind.co.uk/search

import time
import os

os.system('amixer cset numid=1 90%')
os.system("cvlc --play-and-exit bbc_comedy-sou_07005034.mp3")

