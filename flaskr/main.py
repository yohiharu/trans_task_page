#!/usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/make", methods=["POST"])
def make():
    print(request.form.get("text"))
    if request.form.get("text") is None or request.form.get("text") == "":
        return render_template("create.html")
    else:
        return render_template("tasks.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
