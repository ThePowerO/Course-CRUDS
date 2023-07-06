import sqlite3

try:
    bank = sqlite3.connect("students_register.db")
    print("Connected successfully with data bases.")
except sqlite3.Error as error:
    print("Something went wrong: ", error)

try:
    with bank:
        cur = bank.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        duration TEXT,
        price REAL
        )""")
        print("Courses table has been created.")

except sqlite3.Error as erro:
    print("Table creation went wrong: ", erro)

try:
    with bank:
        cur = bank.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course_name TEXT,
        start_date DATE,
        FOREIGN KEY (course_name) REFERENCES courses (name) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Classes table has been created.")

except sqlite3.Error as erro:
    print("Table creation went wrong: ", erro)

try:
    with bank:
        cur = bank.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT,
        image TEXT
        birth_date DATE,
        cpf TEXT,
        class_name TEXT,
        FOREIGN KEY (class_name) REFERENCES classes (name) ON DELETE CASCADE
        )""")
        print("Students table has been created.")

except sqlite3.Error as erro:
    print("Table creation went wrong: ", erro)
