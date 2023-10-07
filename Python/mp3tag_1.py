
import os
import shutil
import glob

# Создаем список файлов mp3 по маске, создаем
# одинаковые названия
filez = glob.glob('E:\English\PimsleurNew\Second\mp3\Pimsleur_II_02-??.mp3')
for file in filez:
    str_list = file.split('-')
    shutil.move(file, '-0'.join(str_list))
print(len(filez))
print(filez)
