from pathlib import Path
import os
import shutil
from striprtf.striprtf import rtf_to_text
# удаляем лишние строки

directory_parent = 'E:\English\PimsleurOld\Pimsleur English for Russian Speakers I (1-30)'
directory_parent_new = 'E:\English\PimsleurNew'

for (parent, directorys, files) in os.walk(directory_parent_new):
    if files:
        for file in files:
            if file.endswith('.txt'):
                big_path_txt = parent + '\\' + file
                with open(big_path_txt, encoding='utf-8') as file_open:
                    list_old = file_open.readlines()
                list_new = [line for line in list_old if (not (
                    'www.spys' in line)) and (not ('азведч' in line))]
                with open(big_path_txt, 'w', encoding='utf-8') as file_open:
                    file_open.writelines(list_new)


def clear_files(what_clear, files=None, directory=None, line_remove=True):
    if not (directory is None):
        for (parent, directorys, list_files) in os.walk(directory):
            if list_files:
                for file in list_files:
                    with open(file, encoding='utf-8') as file_open:
                        list_file = file_open.readlines()
