#!/usr/bin/python3

import sqlite3

def create_table(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks(text, id INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

def create_task(name, task):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("INSERT INTO tasks (text) VALUES ('{}')".format(task))
    con.commit()

def get_tasks(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    res = cur.execute("SELECT text, id FROM tasks")
    return res.fetchall()

def destroy(name, task_id):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id = {}".format(task_id))
    con.commit()

