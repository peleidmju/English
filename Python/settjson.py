import json
import os


path_origin = {}
path_main = 'E:\English\PimsleurNew'
for (parent, directorys, files) in os.walk(path_main):
    if files:
        if not 'PEfRS_' in parent:
            continue
        str_mnl = (int(parent[-1:])-1)*30
        for file in files:
            str_num = int(file[-6:-4]) + str_mnl
            if not str_num in path_origin:
                path_origin[str_num] = {}
            if '.mp3' in file:
                path_origin[str_num]['mp3_origin'] = parent + '\\' + file
            elif '.txt' in file:
                path_origin[str_num]['txt_origin'] = parent + '\\' + file

path_for_json = {}
path_for_json['path_all'] = path_origin
with open('E:\English\Python\settings.json', 'w', encoding='utf-8') as file:
    json.dump(path_for_json, file)
print(path_origin)
