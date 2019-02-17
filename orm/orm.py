import sqlite3

def connect(database):
    #连接到内存或其它地方
    sqlite3.connect(database)

def load_schema(file):
    #在sqlite3下运行 file
    pass

class Person(object):
    #与 person表 对应的 person类
    # id = 0

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def create(self):
        pass
        
