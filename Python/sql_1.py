import sqlite3
import json
import csv
from datetime import datetime as dt

BD_NAME = 'E:\English\Python\\tempfor\sqlite_db.db'
EXC_QUESTENGL = 'E:\Learning\QuestEngl.xlsm'
SCV_QUESTENGL_ENGLISH = 'E:\English\Python\\tempfor\QuestEngl_English.csv'
SCV_QUESTENGL_SpeakEng = 'E:\English\Python\\tempfor\QuestEngl_SpeakEng.csv'
SCV_QUESTENGL_Tests = 'E:\English\Python\\tempfor\QuestEngl_Tests.csv'
TIME_FORMAT = "%d.%m.%Y %H:%M"
# a = '24.07.2023 7:46'
# b = '19.07.2023 21:50'

# print(dt.datetime.strptime(a, "%d.%m.%Y %H:%M"))


def transf_from_testexcell_in_bd():  # заполняем таблицу word_question
    """В базе данных заполняем таблицу word-question
    для этого из эксцеля QuestEngl скачиваем в формате csv листы ('English',
    'SpeakEng' и 'Tests') в папку 'E:\English\Python\\tempfor' с именем QuestEngl_имяЛиста.

    Args:
        EXC_QUESTENGL; 
        SCV_QUESTENGL_ENGLISH; 
        SCV_QUESTENGL_SpeakEng; 
        SCV_QUESTENGL_Tests       
    Returns:
        table word_question
    """    """"""
    scv_English = exc_csv_Eng_English(SCV_QUESTENGL_ENGLISH)
    scv_SpeakEng = exc_csv_Eng_English(SCV_QUESTENGL_SpeakEng)
    scv_Tests = exc_csv_Eng_English(SCV_QUESTENGL_Tests)
    print(scv_Tests)
    with sqlite3.connect(BD_NAME) as conn:
        cursor = conn.cursor()
        querty_check = "SELECT * FROM word_question WHERE question = ? AND answer = ?"
        querty_add = "INSERT INTO word_question VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        querty_update = """UPDATE word_question SET countTrue = ?, countFalse = ?, 
        lastResult = ?, lastDate = ?, comment = ? WHERE id = ?"""

        def start_line(sline):
            start_list = ['' for _ in range(10)]
            start_list[0] = 91
            start_list[3] = sline['Дата']
            start_list[8] = sline['ID']
            return start_list.copy()

        lines = []
        for line in scv_English:
            if line['T1'] != -1:
                start_list_all = start_line(line)
                start_list_all[1] = line['Question']
                start_list_all[2] = line['Answer']
                start_list_all[4] = line['T1']
                start_list_all[5] = line['F1']
                scv_Tests_line = ''
                for test in scv_Tests:
                    if (test['ID_Que'] == start_list_all[8]) and (int(test['1or2']) == 1):
                        if scv_Tests_line:
                            if dt.strptime(scv_Tests_line['Date'], TIME_FORMAT) < dt.strptime(test['Date'], TIME_FORMAT):
                                scv_Tests_line = test.copy()
                        else:
                            scv_Tests_line = test.copy()
                if scv_Tests_line:
                    if scv_Tests_line['Right or Wrong'] == 'Решено':
                        start_list_all[6] = 'True'
                    else:
                        start_list_all[6] = 'False'
                    start_list_all[7] = scv_Tests_line['Date']
                check = cursor.execute(
                    querty_check, (start_list_all[1], start_list_all[2])).fetchall()
                if check:
                    cursor.execute(querty_update, (start_list_all[4], start_list_all[5],
                                                   start_list_all[6], start_list_all[7],
                                                   start_list_all[9], check[0][0]))
                    print(check[0][0])
                else:
                    cursor.execute(querty_add, tuple(start_list_all))
            if line['T2'] != -1:
                start_list_all = start_line(line)
                start_list_all[1] = line['Answer']
                start_list_all[2] = line['Question']
                start_list_all[4] = line['T2']
                start_list_all[5] = line['F2']
                scv_Tests_line = ''
                for test in scv_Tests:
                    if (test['ID_Que'] == start_list_all[8]) and (int(test['1or2']) == 2):
                        if scv_Tests_line:
                            if dt.strptime(scv_Tests_line['Date'], TIME_FORMAT) < dt.strptime(test['Date'], TIME_FORMAT):
                                scv_Tests_line = test.copy()
                        else:
                            scv_Tests_line = test.copy()
                if scv_Tests_line:
                    if scv_Tests_line['Right or Wrong'] == 'Решено':
                        start_list_all[6] = 'True'
                    else:
                        start_list_all[6] = 'False'
                    start_list_all[7] = scv_Tests_line['Date']
                check = cursor.execute(
                    querty_check, (start_list_all[1], start_list_all[2])).fetchall()
                if check:
                    cursor.execute(querty_update, (start_list_all[4], start_list_all[5],
                                                   start_list_all[6], start_list_all[7],
                                                   start_list_all[9], check[0][0]))
                    print(check[0][0])
                    pass
                else:
                    cursor.execute(querty_add, tuple(start_list_all))


# Преобразование листа csvEnglish в список строк
def exc_csv_Eng_English(puth_csv):
    with open(puth_csv, mode='r', encoding='utf-8') as file_csv:
        f_csv = csv.reader(file_csv, delimiter=';')
        name_column = next(f_csv)
        name_column[0] = 'ID'
        print(name_column)
        data_csv = []
        for data in f_csv:
            new_dict = {}
            for i, dat in enumerate(data):
                new_dict[name_column[i]] = dat
            data_csv.append(new_dict)
    return data_csv


transf_from_testexcell_in_bd()


def add_record_courses(record):  # add record table courses
    with sqlite3.connect(BD_NAME) as conn:
        cursor = conn.cursor()
        check = cursor.execute("""SELECT * FROM courses WHERE cours = ? AND level = ? AND
                               lesson = ?""", (record[0], record[1], record[2],)).fetchall()
        if check:
            print("Такая запись есть. Используйте update.")
            return
        query = "INSERT INTO courses VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(query, record)


def create_word_question():  # create table word_question
    with sqlite3.connect(BD_NAME) as conn:
        cursor = conn.cursor()
        query = "DROP TABLE IF EXISTS word_question"
        cursor.execute(query)
        conn.commit()
        query = """CREATE TABLE IF NOT EXISTS word_question (
            id integer PRIMARY KEY,
            lesson integer NOT NULL,
            question text NOT NULL,
            answer text NOT NULL,
            startDate Date,
            countTrue integer NOT NULL,
            countFalse integer NOT NULL,
            lastResult text,
            lastDate Date,
            idExcell integer,
            comment text,
            FOREIGN KEY (lesson) REFERENCES courses(id)
        ) 
"""
        cursor.execute(query)


def add_first_courses():  # добавление первых записей в таблицу courses
    def add_record(table, list_data):
        with sqlite3.connect(BD_NAME) as conn:
            cursor = conn.cursor()
            if table == 'courses':
                for data in list_data:
                    querty_check = """SELECT * FROM courses WHERE cours = ? AND
                        level = ? AND
                        lesson = ?
                    """
                    #                 {data[0]} level = {data[1]} lesson =
                    #                 {data[2]}
                    # """
                    list_new = cursor.execute(
                        querty_check, (data[0], data[1], data[2])).fetchall()
                    if not list_new:
                        querty_check = """INSERT INTO courses VALUES(NULL, ?, ?, ?, ?, ?, False, False, '')"""
                        cursor.execute(querty_check, data)
                conn.commit()

    list_data_new = []
    str_vstavka = ['', 'I', 'II', 'III']
    for level in range(1, 4):
        'PimsleurNew\PEfRS_1\Pimsleur_I_01.mp3'
        str_path_txt = 'E:\English\PimsleurNew\PEfRS_' + \
            str(level) + '\Pimsleur_text_' + str(level) + '_'
        str_path_mp3 = 'E:\English\PimsleurNew\PEfRS_' + \
            str(level) + '\Pimsleur_' + str_vstavka[level] + '_'
        for lesson in range(1, 31):
            record = ('English Pimsler', level, lesson, str_path_txt + str(lesson).zfill(2) +
                      '.txt', str_path_mp3 + str(lesson).zfill(2) + '.mp3')
            list_data_new.append(record)
    add_record('courses', list_data_new)


def create_courses():  # create table courses
    with sqlite3.connect(BD_NAME) as connection:
        cursor = connection.cursor()
        # # Get names tables from db and then delete all tables
        # cursor.execute("SELECT cours FROM sqlite_master WHERE type = 'table'")
        # tables = cursor.fetchall()
        # print(tables)☻
        # for table in tables:
        #     cursor.execute(f"DROP TABLE {table[0]}")
        querty = """CREATE TABLE IF NOT EXISTS courses (
            id integer PRIMARY KEY,
            cours text NOT NULL,
            level integer NOT NULL,
            lesson integer NOT NULL,
            file_text text,
            mp3_text text,
            learning blob DEFAULT FALSE,
            done blob DEFAULT FALSE,
            comment text)
        """
        cursor.execute(querty)


def create_temp_files_lesson():  # create table temp_files_lesson
    with sqlite3.connect(BD_NAME) as connection:
        cursor = connection.cursor()
        querty = """CREATE TABLE IF NOT EXISTS temp_files_lesson (
            id integer PRIMARY KEY,
            lesson integer NOT NULL, 
            fileType text Not NULL,
            filePuth text Not NULL,
            comment text,
            FOREIGN KEY (lesson) REFERENCES courses(id)
            );
        """
        cursor.execute(querty)


def add_first_tflesson():  # Добавление первых записей в таблицу temp_files_lesson
    with open('E:\English\Python\settings.json', 'r') as file:
        data_json = json.load(file)
    data = list(data_json.values())[0]
    print(len(data))
    with sqlite3.connect(BD_NAME) as conn:
        cursor = conn.cursor()
        querty = "INSERT INTO temp_files_lesson VALUES(?, ?, ?, ?, ?);"
        for k_lesson, v in data.items():
            for f_type, f_puth in v.items():
                new_values = (None, k_lesson, f_type, f_puth, '')
                cursor.execute(querty, new_values)
