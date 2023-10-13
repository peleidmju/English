import mp3ask
import glob
import csv
import shutil
import sql_1

file_csv_path = 'E:\English\PimsleurNew\Second\Pimsleur_text_2_02.csv'
file_mp3_path = 'E:\English\PimsleurNew\Second\mp3'

with open(file_csv_path, encoding='utf-8', mode='r') as csv_file:
    reader_csv = csv.reader(csv_file)
    csv_header = next(reader_csv)
    list_csv = []
    for row in reader_csv:
        new_row = {}
        for i, item in enumerate(row):
            new_row[csv_header[i]] = item
        list_csv.append(new_row)
print(len(list_csv))
# print(list_csv)
files_path = glob.glob('E:\English\PimsleurNew\Second\mp3\Pimsleur_32*')
mp3_short = []
for mp3_f in files_path:
    mp3_short.append(mp3ask.Mp3AskShort(mp3_f))
for mp3_f in mp3_short:
    title_current = mp3_f.title
    number_current = int(title_current.partition(' ')[2])
    for scv_line in list_csv:
        if int(scv_line['TimeQuest']) == number_current:
            pass
