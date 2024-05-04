from flask import Flask, render_template, request
# from database import get_job_from_db, save_application_into_db

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/jobs')
def jobs():
    return render_template("jobs.html", page_title="Jobs")

@app.route('/about')
def about():
    return render_template("about.html", page_title="About Us")
