from flask import Flask, render_template, request
# from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__, template_folder='templates')

@app.route("/")
def first_page():
    return render_template("home.html")