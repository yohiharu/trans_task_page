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
    return render_template("create.html", text="")

@app.route("/make", methods=["POST"])
def make():
    text = request.form.get("text")
    language = request.form.get("language")
    if text is None or language is None:
        return render_template("create.html")
    elif len(text) <=30  and language in ["DE", "ZH"]:
        text = translation(text, language)
        db.create_task(db_name, text) 
        return redirect(url_for("tasks"))
    else:
        return render_template("create.html", text=text)

if __name__ == "__main__":
    db.create_table(db_name)
    app.run(host="0.0.0.0", port=80)
