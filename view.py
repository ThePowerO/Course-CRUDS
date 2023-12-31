import sqlite3

try:
    bank = sqlite3.connect("students_register.db")
    print("Connected successfully with data bases.")
except sqlite3.Error as error:
    print("Something went wrong: ", error)

def créer_course(i):
    with bank:
        cur = bank.cursor()
        query = "INSERT INTO Courses (nom, durée, prix) VALUES (?,?,?)"
        cur.execute(query, i)

#créer_course(["Python", "2 Weeks", 50])
def voir_courses():
    list = []
    with bank:
        cur = bank.cursor()
        cur.execute("SELECT * FROM Courses")
        ligne = cur.fetchall()

        for i in ligne:
            list.append(i)
    return list

print(view_courses())

def update_course(i):
    with bank:
        cur = bank.cursor()
        query = "UPDATE Courses SET nom=?, durée=?, prix=? WHERE id=?"
        cur.execute(query, i)

#update_course(i)

def supprimer_course(i):
    with bank:
        cur = bank.cursor()
        query = "DELETE FROM Courses WHERE id=?"
        cur.execute(query, i)

supprimer_course([1])


def créer_class(i):
    with bank:
        cur = bank.cursor()
        query = "INSERT INTO Classes (nom, cours_nom, date_initiale) VALUES (?,?,?)"
        cur.execute(query, i)

def voir_classes():
    list = []
    with bank:
        cur = bank.cursor()
        cur.execute("SELECT * FROM Classes")
        ligne = cur.fetchall()

        for i in ligne:
            list.append(i)
    return list

def update_classes(i):
    with bank:
        cur = bank.cursor()
        query = "UPDATE Classes SET nom=?, cours_nom=?, date_initiale=? WHERE id=?"
        cur.execute(query, i)

def supprimer_classes(i):
    with bank:
        cur = bank.cursor()
        query = "DELETE FROM Classes WHERE id=?"
        cur.execute(query, i)


def crée_étudiants(i):
    with bank:
        cur = bank.cursor()
        query = "INSERT INTO étudiants (nom, email, téléphone, genre, image, date_naissance, cpf, class_nom) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

def voir_étudiants():
    list =  []
    with bank:
        cur = bank.cursor()
        cur.execute("SELECT * FROM étudiants")
        ligne = cur.fetchall()

        for i in ligne:
            list.append(i)
    return list

def update_étudiants(i):
    with bank:
        cur = bank.cursor()
        query = "UPDATE étudiants SET nom=?, email=?, téléphone=?, genre=?, image=?, date_naissance=?, cpf=?, class_nom=? WHERE id=?"
        cur.execute(query, i)

def supprimer_étudiants(i):
    with bank:
        cur = bank.cursor()
        query = "DELETE FROM Étudiants WHERE id=?"
        cur.execute(query, i)
