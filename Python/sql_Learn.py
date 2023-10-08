import sqlite3

DB_NAME_TEMP = 'Python\\tempfor\sqlite_db.db'

# # crearte table
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

# # get time and date
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     cursor = sqlite_conn.cursor()
#     query = "SELECT datetime('now', 'localtime');"
#     results = cursor.execute(query)
#     row = results.fetchone()
#     time = row[0]
#     print(time)

# Add records to the courses table variant 1
courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35),
    (251, "Python course", 100, 30),
]
with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    sql_request_check = "SELECT * FROM courses WHERE id = ?"
    cursor = sqlite_conn.cursor()
    for course in courses:
        id_true = cursor.execute(sql_request_check, (course[0],)).fetchall()
        if id_true:
            continue
        else:
            continue
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
    sqlite_conn.commit()

# # Add records to the courses table variant 2
# courses = [
#     (351, "JavaScript course", 415, 100),
#     (614, "C++ course", 161, 10),
#     (721, "Java full course", 100, 35),
#     (251, "Python course", 100, 30),
# ]
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     cursor = sqlite_conn.cursor()
#     cursor.executemany(sql_request, courses)

# # Update records
# update_record = (90, 'Python course')
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     cursor = sqlite_conn.cursor()
#     sql_request = "UPDATE courses SET students_qty = ? WHERE title = ?;"
#     cursor.execute(sql_request, update_record)

# # Delete records
# delete_record = ('C++ course', 'Python course')
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     cursor = sqlite_conn.cursor()
#     sql_request = "DELETE FROM courses WHERE title IN ('C++ course', 'Python course')"
#     cursor.execute(sql_request)

# # read table
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     sql_request = "SELECT * FROM courses"
#     sql_cursor = sqlite_conn.execute(sql_request)
#     # for record in sql_cursor:
#     #     print(record)
#     records = sql_cursor.fetchall()
#     print(records)

# # run script SQL
# sql = """
#     DROP TABLE IF EXISTS People;
#     CREATE TABLE IF NOT EXISTS People(
#         FirstName TEXT,
#         LastName TEXT,
#         Age INT
#     );
#     INSERT INTO People VALUES(
#         'Ron',
#         'Obvious',
#         '42'
#     );
# """
# with sqlite3.connect(DB_NAME_TEMP) as connection:
#     cursor = connection.cursor()
#     cursor.executescript(sql)

# # delete table
# with sqlite3.connect(DB_NAME_TEMP) as sqlite_conn:
#     cursor = sqlite_conn.cursor()
#     query = "DROP TABLE courses;"
#     cursor.execute(query)
#     sqlite_conn.commit()
