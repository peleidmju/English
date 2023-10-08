import sqlite3


BD_NAME = 'E:\English\Python\\tempfor\sqlite_db.db'

# # добавление новых записей в таблицу courses
# def add_record(table, list_data):
#     with sqlite3.connect(BD_NAME) as conn:
#         cursor = conn.cursor()
#         if table == 'courses':
#             for data in list_data:
#                 querty_check = """SELECT * FROM courses WHERE name = ? AND
#                     level = ? AND
#                     lesson = ?
#                 """
#                 #                 {data[0]} level = {data[1]} lesson =
#                 #                 {data[2]}
#                 # """
#                 list_new = cursor.execute(
#                     querty_check, (data[0], data[1], data[2])).fetchall()
#                 if not list_new:
#                     querty_check = """INSERT INTO courses VALUES(NULL, ?, ?, ?, ?, ?, False, False, '')"""
#                     cursor.execute(querty_check, data)
#             conn.commit()
# list_data_new = []
# str_vstavka = ['', 'I', 'II', 'III']
# for level in range(1, 4):
#     'PimsleurNew\PEfRS_1\Pimsleur_I_01.mp3'
#     str_path_txt = 'E:\English\PimsleurNew\PEfRS_' + \
#         str(level) + '\Pimsleur_text_' + str(level) + '_'
#     str_path_mp3 = 'E:\English\PimsleurNew\PEfRS_' + \
#         str(level) + '\Pimsleur_' + str_vstavka[level] + '_'
#     for lesson in range(1, 31):
#         record = ('English Pimsler', level, lesson, str_path_txt + str(lesson).zfill(2) +
#                   '.txt', str_path_mp3 + str(lesson).zfill(2) + '.mp3')
#         list_data_new.append(record)
# add_record('courses', list_data_new)

# with sqlite3.connect(BD_NAME) as connection:
#     cursor = connection.cursor()
#     # # Get names tables from db and then delete all tables
#     # cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
#     # tables = cursor.fetchall()
#     # print(tables)☻
#     # for table in tables:
#     #     cursor.execute(f"DROP TABLE {table[0]}")
#     querty = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         name text NOT NULL,
#         level integer NOT NULL,
#         lesson integer NOT NULL,
#         file_text text,
#         mp3_text text,
#         learning blob DEFAULT FALSE,
#         done blob DEFAULT FALSE,
#         comment text)
#     """
#     cursor.execute(querty)
