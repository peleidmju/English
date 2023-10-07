import pprint as pp
import re
import csv
# запись для ексцеля


def open_file(path):

    with open(path, encoding='utf-8') as file:
        return file.read()


def write_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


old_path = 'E:\English\Python\\tempfor\Pimsleur_text_2b_02.txt'
new_path = 'E:\English\Python\\tempfor\Pimsleur_text_2c_02.txt'
csv_path = 'E:\English\Python\\tempfor\Pimsleur_text_2_02.csv'

my_text = open_file(old_path)
# list_my_text = my_text.split('\n')

my_pattern = re.compile(
    r'(?m)^\d*\t1\t\d*\t(?P<timeQuest>[^\t]+)\t(?P<Question>[^\n]+)\n\d*\t2\t\d*\t(?P<timeAns>[^\t]+)\t(?P<Answer>[^\n]+)\n(\d+\t\t\d+\t(?P<timeTemp>[^\t]*))?')
list_my_text = list(re.finditer(my_pattern, my_text))
print(len(list_my_text))
dict_my_text = [item.groupdict() for item in list_my_text]
pp.pprint(dict_my_text)
subject = 'Lesson_32'
new_text = ''
for item in dict_my_text:
    new_text += subject + '\t' + \
        item['Answer'] + '\t' + item['Question'] + '\n'
# write_file(new_path, new_text)
# for item in dict_my_text:
#     new_text += subject + '\t' + item['timeQuest'] + '\t' + \
#         item['Answer'] + '\t' + item['Question'] + '\n'
write_file(new_path, new_text)


headers = ['Number', 'Subject', 'TimeQuest',
           'Question', 'Answer', 'TimeTemp']
rows = []
time_temp = '0'
line_not = False
row_old = ''
for i, item in enumerate(dict_my_text):
    if line_not:
        row = (*row_old, item['timeQuest'])
        rows.append(row)
        line_not = False
    if item['timeTemp']:
        row = (i, subject, item['timeQuest'],
               item['Question'], item['Answer'], item['timeTemp'])
        rows.append(row)
    else:
        row_old = [i, subject, item['timeQuest'],
                   item['Question'], item['Answer']]
        line_not = True

with open(csv_path, mode='w', encoding='utf-8') as file:
    file_csv = csv.writer(file)
    file_csv.writerow(headers)
    file_csv.writerows(rows)
