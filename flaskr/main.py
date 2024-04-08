#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import db
from api.api import translation

app = Flask(__name__)
db_name = "database.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def tasks():
    tasks = [ i[0] for i in db.get_tasks(db_name) ]
    tasks.reverse()
    return render_template("tasks.html", tasks=tasks)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/make", methods=["POST"])
def make():
    if request.form.get("text") is None or request.form.get("text") == "":
        return render_template("create.html")
    else:
        text = translation(request.form.get("text"), "ZH")
        db.create_task(db_name, text) 
        return redirect(url_for("tasks"))

if __name__ == "__main__":
    db.create_table(db_name)
    app.run(host="0.0.0.0", port=80)
