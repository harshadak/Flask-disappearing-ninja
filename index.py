from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    message = "none"
    return render_template("index.html", message = message)

@app.route("/ninja")
def ninja():
    return render_template("index.html", message = "all")

@app.route("/ninja/<color>")
def ninjaColor(color):
    return render_template("index.html", color = color)

app.run(debug = True)