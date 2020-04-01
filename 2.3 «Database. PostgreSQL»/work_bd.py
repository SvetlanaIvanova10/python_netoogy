# Схемы:
#
# Student:
#  id     | integer                  | not null
#  name   | character varying(100)   | not null
#  gpa    | numeric(10,2)            |
#  birth  | timestamp with time zone |
#
# Course:
#  id     | integer                  | not null
#  name   | character varying(100)   | not null
import psycopg2 as pg
from pprint import pprint


def create_db(): # создает таблицы
    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute("""CREATE TABLE IF NOT EXISTS Student 
            (id serial PRIMARY KEY , 
            name varchar(100) NOT NULL, 
            gpa numeric(10, 2) NULL, 
            birth timestamp with time zone NULL);""")
            curs.execute("""CREATE TABLE IF NOT EXISTS Course
            (id serial PRIMARY KEY ,
            name character varying(100) NOT NULL);""")
            curs.execute("""CREATE TABLE IF NOT EXISTS Student_course 
            (id serial PRIMARY KEY,
            student_id INTEGER REFERENCES Student(id),
            course_id INTEGER REFERENCES  Course(id));""")

            curs.execute("select * from Student")
            stud = curs.fetchall()
            pprint(stud)

            curs.execute("select * from Course")
            cour = curs.fetchall()
            pprint(cour)

            curs.execute("select * from Student_course")
            cour_stud = curs.fetchall()
            pprint(cour_stud)

course = {}
def add_course(course): # просто создает курс
    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute("insert into Course (name) values (%s)", (course['name'],))
            curs.execute("select * from Course")
            list_course = curs.fetchall()
            pprint(list_course)
            return list_course

def get_students(course_id): # возвращает студентов определенного курса
    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute(" SELECT student_id FROM Student_course WHERE course_id = (%s)", (course_id,))
            stud_curs = curs.fetchall()
            for number_id in stud_curs:
                curs.execute("select * from Student where id = (%s)", number_id)
                stud_one_curs = curs.fetchall()
                print(stud_one_curs)

students = {}
def add_students(course_id, students): # создает студентов и
                                       # записывает их на курс

    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute("insert into Student (name, birth, gpa) values (%s, %s, %s)", (students['name'], students['birth'], students['gpa']))
            curs.execute("select * from student")
            stud = curs.fetchall()
            curs.execute("insert into Student_course (student_id, course_id) values (%s, %s)", (stud[-1][0], course_id))
            curs.execute("""select s.id, s.name, c.name from student_course sc
            join student s on s.id = sc.student_id 
            join course c on c.id = sc.course_id""")
            curs_stud = curs.fetchall()
            pprint(curs_stud)

student = {}
def add_student(student): # просто создает студента
    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute("insert into Student (name, birth, gpa) values (%s, %s, %s)", (student['name'], student['birth'], student['gpa']))
            curs.execute("select * from Student")
            stud = curs.fetchall()
            pprint(stud)


def get_student(student_id):
    with pg.connect("dbname = test_db user = test password = 1234") as conn:
        with conn.cursor() as curs:
            curs.execute("select * from Student")
            stud = curs.fetchall()
            for rowcount in stud:
                for id_stud in rowcount:
                    if id_stud == student_id:
                        print(rowcount)



if __name__ == '__main__':
    create_db()
    add_student({'name': 'Sveta3', 'birth': '2.10.1997', 'gpa': 65})
    add_students(2, {'name': 'Sveta4', 'birth': '02.10.1997', 'gpa': 35})
    add_course({'name': 'с++'})
    get_student(1)
    get_students(1)

