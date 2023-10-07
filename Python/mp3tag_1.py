
import os
import shutil
import glob

# Создаем список файлов mp3 по маске, создаем
# одинаковые названия
filez = glob.glob('E:\English\PimsleurNew\Second\mp3\Pimsleur_II_02-??.mp3')
for file in filez:
    str_list = file.split('-')
    shutil.move(file, '-0'.join(str_list))
# filez = glob.glob('E:\English\PimsleurNew\Second\mp3\Pimsleur_II_02-*.mp3')
filez = glob.glob('E:\English\Python\\tempfor\Pimsleur_II_02-*.mp3')
for file in filez:
    str_list_1 = file.split('_', 1)
    str_list_2 = str_list_1[1].split('-')
    shutil.move(file, str_list_1[0] + '_32-' + str_list_2[1])
    # print(str_list_1[0] + '_32-' + str_list_2[1])
print(len(filez))
# print(filez)
