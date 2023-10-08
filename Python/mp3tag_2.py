from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
from mutagen.id3 import ID3

import os
import shutil
import glob
import csv

# Работаем с тегами файлов mp3, уже разбитыми на
# маленькие звуковые файлы.
filez = glob.glob('E:\English\Python\\tempfor\Pimsleur_32-*.mp3')
count_filez = len(filez)
str_count_filez = str(count_filez)
mp3file = MP3(filez[124], ID3=EasyID3)
print(mp3file)
csv_file_list = []
with open('E:\English\Python\\tempfor\Pimsleur_text_2_02.csv', encoding='utf-8') as file:
    file_csv_reader = csv.DictReader(file)
    for line in file_csv_reader:
        csv_file_list.append(line)
print(csv_file_list)
for i in range(coun
               
               t_filez):
    tracknumber = str(i+1).zfill(len(str_count_filez)) + '/' + str_count_filez
    mp3file = MP3(filez[i], ID3=EasyID3)
    mp3file['album'] = 'Lesson 32'
    mp3file['artist'] = 'Pimsler 2'
    mp3file['genre'] = 'English'
    mp3file['tracknumber'] = tracknumber
    mp3file.save()
