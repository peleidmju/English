from mp3ask import Mp3AskShort, Lesson, Cours
import glob
import csv
import shutil
import sql_1
import datetime
import copy


file_csv_path = 'E:\English\Python\\tempfor\mp3\Pimsleur_text_2_02.csv'
file_mp3_path = 'E:\English\PimsleurNew\Second\mp3'
files_path = glob.glob('E:\English\Python\\tempfor\mp3\Pimsleur_32*')
"""{'album': ['Vinyl #2'], 'bpm': ['Poo'], 
'composer': ['Poo'], 'length': ['100000'], 
'title': ['Рокки'], 'artist': ['Zivert'], 
'albumartist': ['Zivert_2'], 
'conductor': ['Poo'], 'discnumber': ['1'], 
'organization': ['111555'], 
'tracknumber': ['1'], 
'isrc': ['RUB422101653'], 'genre': ['Поп'], 
'date': ['2021-10-08'], 
'barcode': ['5057827893006']}
"""


def proba():
    mus = Mp3AskShort("D:\\Music\\01 - Рокки.mp3")
    stroka = ''
    dict_tag = {}
    i = 0
    mus.mp3tag_save(**{'title': 'Рокки'})
    # while True:
    #     i += 100
    #     if i == 10000000:
    #         break
    #     stroka += 's'
    #     dict_tag['length'] = str(i)
    #     mus.mp3tag_save(**dict_tag)
    #     print(len(mus.mp3tag(tag='length')[0]))
    # # print(mus.mp3tag(tag='album'))
    print(mus.mp3tag())
    # print(mus.length())


# proba()


def get_list_csv():
    with open(file_csv_path, encoding='utf-8', mode='r') as csv_file:
        reader_csv = csv.reader(csv_file)
        csv_header = next(reader_csv)
        list_csv = []
        for row in reader_csv:
            new_row = {}
            for i, item in enumerate(row):
                new_row[csv_header[i]] = item
            list_csv.append(new_row)
    return list_csv
# print(list_csv)

# mp3ask.Mp3AskShort.mp3tag()


def get_list_mp3(path):
    mp3_short = []
    for mp3_f in path:
        mp3_short.append(Mp3AskShort(mp3_f))
    return mp3_short


def files_into_bd():
    for mp3_f in mp3_short:
        title_current = mp3_f.title
        number_current = int(title_current.partition(' ')[2])
        for scv_line in list_csv:
            if not scv_line:
                continue
            if int(scv_line['TimeQuest']) == number_current:
                id_cur = sql_1.update_mp3short(lesson=scv_line['Subject'], question=scv_line['Question'],
                                               answer=scv_line['Answer'], path=mp3_f.path, length=mp3_f.length())
                print(mp3_f.mp3tag())


def write_tag_csv_bd_new():
    cours_cur = Cours("Pimsler English")
    lesson_cur = Lesson(cours_cur, 'Lesson_32')
    mp3files = get_list_mp3(files_path)
    csvlist = get_list_csv()
    csvlist_new = []
    dict_for_lesson = {}
    for i, mp3file in enumerate(mp3files, start=1):
        dict_for_lesson[i] = {}
        dict_for_lesson[i]['pathmp3'] = mp3file.path
        dict_for_lesson[i]['tag'] = {}
        dict_for_lesson[i]['csv'] = {}
        num_isrc = mp3file.isrc
        # if (not num_isrc) or (not 'isrc' in csvlist[i-1]):
        num_zvuk = mp3file.title
        num_zvuk = int(num_zvuk.partition(' ')[2])
        key_scv = 'TimeQuest'
        # else:
        #     num_zvuk = num_isrc
        #     key_scv = 'isrc'
        for line in csvlist:
            if line[key_scv] == str(num_zvuk):
                dict_for_lesson[i]['tag']['title'] = line['Question']
                dict_for_lesson[i]['tag']['artist'] = cours_cur.cours
                dict_for_lesson[i]['tag']['album'] = lesson_cur.lesson
                dict_for_lesson[i]['tag']['length'] = mp3file.length
                dict_for_lesson[i]['tag']['composer'] = line['Answer']
                dict_for_lesson[i]['tag']['tracknumber'] = i
                dict_for_lesson[i]['tag']['date'] = str(
                    datetime.datetime.now()).rpartition('.')[0]
                dict_for_lesson[i]['csv']['Number'] = i
                dict_for_lesson[i]['csv']['Subject'] = lesson_cur.lesson
                dict_for_lesson[i]['csv']['TimeQuest'] = line['TimeQuest']
                dict_for_lesson[i]['csv']['Question'] = line['Question']
                dict_for_lesson[i]['csv']['Answer'] = line['Answer']
                dict_for_lesson[i]['csv']['TimeTemp'] = line['TimeTemp']
                dict_for_lesson[i]['csv']['Cours'] = cours_cur.cours
                dict_for_lesson[i]['csv']['Length'] = dict_for_lesson[i]['tag']['length']
                dict_for_lesson[i]['csv']['Date'] = dict_for_lesson[i]['tag']['date']
                dict_for_lesson[i]['csv']['Path'] = dict_for_lesson[i]['pathmp3']
                num_bd = sql_1.update_mp3short(cours=cours_cur.cours, lesson=lesson_cur.lesson,
                                               question=line['Question'], answer=line['Answer'],
                                               path=dict_for_lesson[i]['pathmp3'],
                                               length=dict_for_lesson[i]['tag']['length'],
                                               )
                dict_for_lesson[i]['tag']['barcode'] = num_bd
                dict_for_lesson[i]['csv']['NumberBD'] = num_bd
                break
        # csvlist_new.append(copy.deepcopy(dict_for_lesson))
    print(dict_for_lesson)
    header_csv_row = ['Number', 'Subject', 'Answer', 'Question', 'TimeQuest', 'TimeTemp',
                      'Cours', 'Length', 'Date', 'Path', 'NumberBD']
    for_file_csv = []
    for_file_csv.append(header_csv_row)
    number_row = 1
    while number_row in dict_for_lesson.keys():
        row = dict_for_lesson[number_row]
        new_row = []
        for header in header_csv_row:
            new_row.append(row['csv'][header])
        for_file_csv.append(new_row.copy())
        number_row += 1
    with open(file_csv_path, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(for_file_csv)


# mp3file.isrc = str(i)
print(datetime.datetime.now())
write_tag_csv_bd_new()
