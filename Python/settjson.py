import json
import os
# это третий файл для работы

path_origin = {}
path_main = 'E:\English\PimsleurNew'
for (parent, directorys, files) in os.walk(path_main):
    if files:
        if not 'PEfRS_' in parent:
            continue
        str_mnl = (int(parent[-1:])-1)*30
        for file in files:
            if not file[-6:-4].isnumeric():
                continue
            str_num = 'Lesson_' + str(int(file[-6:-4]) + str_mnl).zfill(2)
            if not str_num in path_origin:
                path_origin[str_num] = {}
            if '.mp3' in file:
                path_origin[str_num]['mp3_origin'] = parent + '\\' + file
            elif '.txt' in file:
                path_origin[str_num]['txt_origin'] = parent + '\\' + file
for (parent, directorys, files) in os.walk('E:\English\PimsleurNew\First'):
    if files:
        for file in files:
            str_num = 'Lesson_' + file[-6:-4].zfill(2)
            if not str_num in path_origin:
                path_origin[str_num] = {}
            if '.csv' in file:
                path_origin[str_num]['csv_for_mp3'] = parent + '\\' + file
            elif '.txt' in file:
                if file[-8:-6] == 'a_':
                    path_origin[str_num]['txt_stepA_edit'] = parent + \
                        '\\' + file
                elif file[-8:-6] == 'b_':
                    path_origin[str_num]['txt_stepB_edit'] = parent + \
                        '\\' + file
                elif file[-8:-6] == 'c_':
                    path_origin[str_num]['txt_stepC_edit'] = parent + \
                        '\\' + file
for (parent, directorys, files) in os.walk('E:\English\PimsleurNew\Second'):
    if files:
        for file in files:
            if '.mp3' in file:
                continue
            str_num = 'Lesson_' + str(int(file[-6:-4])+30).zfill(2)
            if not str_num in path_origin:
                path_origin[str_num] = {}
            if '.csv' in file:
                path_origin[str_num]['csv_for_mp3'] = parent + '\\' + file
            elif '.txt' in file:
                if file[-8:-6] == 'a_':
                    path_origin[str_num]['txt_stepA_edit'] = parent + \
                        '\\' + file
                elif file[-8:-6] == 'b_':
                    path_origin[str_num]['txt_stepB_edit'] = parent + \
                        '\\' + file
                elif file[-8:-6] == 'c_':
                    path_origin[str_num]['txt_stepC_edit'] = parent + \
                        '\\' + file
path_for_json = {}
path_for_json['Pimsler English'] = path_origin
path_for_json['Programming'] = {}
path_for_json['Programming']['Programming'] = {}

with open('E:\English\Python\settings.json', 'w', encoding='utf-8') as file:
    json.dump(path_for_json, file)
print(path_for_json)
