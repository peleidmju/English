import glob
import shutil

TXT_START = 'E:\English\PimsleurNew\PEfRS_3\Pimsleur_text_3_30.txt'
TXT_PREVIEW = 'E:\English\Python\\tempfor\\Pimsleur_text_a_36.txt'
TXT_PREVIEW_CHECK = 'E:\English\Python\\tempfor\\Pimsleur_text_aa_36.txt'
ALPHABET_RUSSIAN = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def rename_mp3():
    files = glob.glob("E:\English\PimsleurNew\Second\mp3\Pimsleur_35_*.mp3")
    for file in files:
        new_name = ((file.split('_')[2]).split('.')[0]).zfill(3)
        new_name = file.split('_')[0] + '_35-' + new_name + '.mp3'
        shutil.move(file, new_name)


def preview():
    # with open(TXT_START, mode='r') as file:
    # print(ord('‐'))
    # print(ord('–'))
    temp_line = ''
    with open(TXT_START, encoding='utf-8', mode='r') as file:
        all_txt_start = file.readlines()
    txt_start_v2 = []
    for i, line in enumerate(all_txt_start, 1):
        temp_line = line
        if '…' in temp_line:
            temp_line = temp_line.replace('…', "...")
        if '’' in temp_line:
            temp_line = temp_line.replace('’', "'")
        if '‘' in temp_line:
            temp_line = temp_line.replace('‘', "'")
        if '–' in temp_line:
            temp_line = temp_line.replace('–', "-")
        if '‐' in temp_line:
            temp_line = temp_line.replace('‐', "-")
        if '«' in temp_line:
            temp_line = temp_line.replace('«', '"')
        if '»' in temp_line:
            temp_line = temp_line.replace('»', '"')
        count_not_ascii, temp_line_2 = 0, ''
        for char in temp_line:
            if ord(char) > 127:
                count_not_ascii += 1
                temp_line_2 += '^'
            temp_line_2 += char
        if count_not_ascii and (count_not_ascii*5 < len(temp_line)):
            temp_line = temp_line_2
            print(i, temp_line)
        txt_start_v2.append(temp_line + '№')
    with open(TXT_PREVIEW, encoding='utf-8', mode='w') as file:
        file.writelines(txt_start_v2)


# rename_mp3()
preview()
