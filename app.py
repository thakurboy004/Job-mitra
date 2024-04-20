from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def first_page():
    return render_template("home.html")