import pprint as pp
# запись файла для ручной правки
# первый файл для работы


def open_file(path):

    with open(path, encoding='utf-8') as file:
        return file.read()


def write_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


old_path = 'E:\English\PimsleurNew\PEfRS_1\Pimsleur_text_1_26.txt'
new_path = 'E:\English\Python\\tempfor\Pimsleur_text_1a_26.txt'
my_text = open_file(old_path)

num_block, num_space, blEnd = 0, 0, True
dict_text = {}
list_text = my_text.split('\n')
print(len(list_text))
for line in list_text:
    if blEnd:
        if line == '':
            continue
        num_block += 1
        new_block = []
        new_block.append(line)
        num_space = 0
        blEnd = False
        continue
    else:
        if line == '':
            if num_space == 0:
                num_space = 1
                new_block.append(line)
                continue
            else:
                new_block.pop()
                dict_text[num_block] = new_block
                blEnd = True
                continue
        else:
            num_space = 0
            new_block.append(line)
            continue
print(len(dict_text))
pp.pprint(dict_text)
new_text = ''
for k, v in dict_text.items():
    num_line = 1
    for line in v:
        if line == '':
            continue
        new_text += str(k) + '\t'
        if num_line < 3:
            new_text += str(num_line)
        new_text += '\t' + str(len(line)) + '\t' + '0' + '\t' + line + '\n'
        if len(line) < 80:
            num_line += 1

write_file(new_path, new_text)
