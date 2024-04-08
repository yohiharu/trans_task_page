#!/usr/bin/python3

import sqlite3

def create_table(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("CREATE TABLE tasks(text)")

def create_task(name, text):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("INSERT INTO tasks (text) VALUES ({})".format(text))
    con.commit()

def get_tasks(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    res = cur.execute("SELECT text FROM tasks")
    return res
