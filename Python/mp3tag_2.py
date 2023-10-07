from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from mutagen.id3 import ID3

import os
import shutil
import glob

# Работаем с тегами файлов mp3
filez = glob.glob('E:\English\Python\\tempfor\Pimsleur_II_02-*.mp3')
print(len(filez))
mp3file = MP3(filez[1], ID3=EasyID3)
print(mp3file)
