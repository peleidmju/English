import sqlite3
import json
import csv

BD_NAME = 'E:\English\Python\\tempfor\sqlite_db.db'
EXC_QUESTENGL = 'E:\Learning\QuestEngl.xlsm'
SCV_QUESTENGL_ENGLISH = 'E:\English\Python\\tempfor\QuestEngl_English.csv'


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
