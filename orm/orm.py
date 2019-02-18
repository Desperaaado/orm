import sqlite3
from os import path

CONN = None

def connect(database):
    #连接到内存或其它地方
    global CONN
    CONN = sqlite3.connect(database)

def load_schema(file_name):
    #在sqlite3下运行 file
    cur = CONN.cursor()
    script = open(file_name).read()
    cur.executescript(script)
    CONN.commit()

class Person(object):
    #与 person表 对应的 person类

    def __init__(self, fname, lname, age):
        self.pk = None
        self.fname = fname
        self.lname = lname
        self.age = age

    def create(self):
        cur = CONN.cursor()
        cur.execute('insert into person(fname, lname, age) values(?,?,?)',
                    (self.fname, self.lname, self.age))
        self.pk = cur.lastrowid
        print('>>>', self.pk)
        CONN.commit()

    def update(self):
        cur = CONN.cursor()
        cur.execute('update person set fname=?, lname=?, age=? where id=?',
                    (self.fname, self.lname, self.age, self.pk))
        CONN.commit()

    def delete(self):
        cur = CONN.cursor()
        cur.execute('delete from person where id=?', (self.pk,))
        CONN.commit()

    @classmethod
    def read(self, pk):
        cur = CONN.cursor()
        cur.execute('select id, fname, lname, age from person where id=?',
                    (pk,))
        row = cur.fetchone()
        obj = Person(*row[1:])
        obj.pk = row[0]
        return obj