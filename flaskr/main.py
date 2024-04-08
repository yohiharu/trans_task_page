#!/usr/bin/python3

from flask import Flask, render_template, request
import db

app = Flask(__name__)
db_name = "database.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def tasks():
    print(db.get_tasks(db_name))
    return render_template("tasks.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/make", methods=["POST"])
def make():
    if request.form.get("text") is None or request.form.get("text") == "":
        return render_template("create.html")
    else:
        db.create_task(db_name, request.form.get("text")) 
        return render_template("tasks.html")

if __name__ == "__main__":
    db.create_table(db_name)
    app.run(host="0.0.0.0", port=80)
