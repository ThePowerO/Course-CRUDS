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
        nom TEXT,
        durée TEXT,
        prix REAL
        )""")
        print("La table des courses a été créée.")

except sqlite3.Error as erreur:
    print("La création de la table a mal tourné: ", erreur)

try:
    with bank:
        cur = bank.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        cours_nom TEXT,
        date_initiale DATE,
        FOREIGN KEY (cours_nom) REFERENCES courses (nom) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("La table des classes a été créée.")

except sqlite3.Error as erreur:
    print("La création de la table a mal tourné: ", erreur)

try:
    with bank:
        cur = bank.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS étudiants(id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        email TEXT,
        téléphone TEXT,
        genre TEXT,
        image TEXT,
        date_naissance DATE,
        cpf TEXT,
        class_nom TEXT,
        FOREIGN KEY (class_nom) REFERENCES classes (nom) ON DELETE CASCADE
        )""")
        print("La table des étudiants a été créée.")

except sqlite3.Error as erreur:
    print("La création de la table a mal tourné: ", erreur)
