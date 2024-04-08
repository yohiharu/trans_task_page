#!/usr/bin/python3

import sqlite3

def create_table(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks(text)")
    con.commit()

def create_task(name, task):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("INSERT INTO tasks VALUES ('{}')".format(task))
    con.commit()

def get_tasks(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    res = cur.execute("SELECT text FROM tasks")
    return res.fetchall()
