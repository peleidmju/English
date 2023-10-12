import pprint as pp
"""
После копирования перевода в файл '*a_*.txt' обрабатываем его
"""


def open_file(path):

    with open(path, encoding='utf-8') as file:
        return file.readlines()


def write_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(text))


old_path = 'E:\English\Python\\tempfor\Pimsleur_text_2a_03.txt'
new_path = 'E:\English\Python\\tempfor\Pimsleur_text_2b_03.txt'
my_list = open_file(old_path)
my_list_eng = my_list[0:((len(my_list))//2)]
my_list_rus = my_list[((len(my_list))//2):]
for i in range(0, len(my_list_rus), 2):
    str_eng = my_list_eng[i+1].rpartition('\t')
    str_rus = my_list_rus[i+1][len(str_eng[0])+1:-1]
    str_eng_2 = my_list_eng[i].rpartition('\t')
    str_eng_3 = str_eng_2[0].split('\t')
    my_list_eng[i] = str_eng_3[0] + '\t' + str_eng_3[1] + \
        '\t' + str(len(str_rus)) + '\t\t' + str_rus
    # my_list_eng[i] = str_eng_2[0] + '\t' + str_rus
    if my_list_eng[i+1].endswith('\n'):
        my_list_eng[i+1] = my_list_eng[i+1][:-1]
# my_list_rus = my_list[(len(my_list)/2):]
print(my_list_eng)

write_file(new_path, my_list_eng)
