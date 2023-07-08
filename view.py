import sqlite3

try:
    bank = sqlite3.connect("students_register.db")
    print("Connected successfully with data bases.")
except sqlite3.Error as error:
    print("Something went wrong: ", error)

def create_course(i):
    with bank:
        cur = bank.cursor()
        query = "INSERT INTO Courses (name, duration, price) VALUES (?,?,?)"
        cur.execute(query, i)

#create_course(["Python", "2 Weeks", 50])
def view_courses():
    list = []
    with bank:
        cur = bank.cursor()
        cur.execute("SELECT * FROM Courses")
        row = cur.fetchall()

        for i in row:
            list.append(i)
    return list

print(view_courses())

def update_course(i):
    with bank:
        cur = bank.cursor()
        query = "UPDATE Courses SET name=?, duration=?, price=? WHERE id=?"
        cur.execute(query, i)

i = ["Python", "1 Month", 50, 1]
#update_course(i)

def delete_course(i):
    with bank:
        cur = bank.cursor()
        query = "DELETE FROM Courses WHERE id=?"
        cur.execute(query, i)

delete_course([1])

def create_class(i):
    with bank:
        cur = bank.cursor()
        query = "INSERT INTO Classes (name, course_name, start_date) VALUES (?,?,?)"
        cur.execute(query, i)

def view_classes():
    list[]
    with bank:
