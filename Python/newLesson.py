from striprtf.striprtf import rtf_to_text
import pprint as pp


with open('Pimsleur English for Russian Speakers I (1-30)\Pimsleur_text_1st_lesson.doc') as file:
    new_text = rtf_to_text(file.read())

print(new_text)


def clearSerov(text):
    line_text = text.split('\n')
    # pp.pprint(line_text)
    clear = ["Школа Разведчика с Игорем Серовым", 'http://spyschool.ru/']
    clear_text = []
    for item in line_text:
        for cl in clear:
            if cl in item:
                break
        else:
            clear_text.append(item)
    return clear_text


pp.pprint(clearSerov(new_text))
