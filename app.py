from flask import Flask, render_template, request
from database import get_job_from_db, save_application_into_db, load_jobs_from_db

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route('/jobs')
def jobs():
    jobs = load_jobs_from_db()
    return render_template("jobs.html", page_title="Jobs", jobs=jobs)

@app.route('/about')
def about():
    return render_template("about.html", page_title="About Us")

@app.route('/job/<id>')
def load_job(id):
    job = get_job_from_db(id)
    return render_template("job.html", page_title=job[1], job=job)

@app.route('/apply/<id>', methods=['POST'])
def apply(id):
    job = get_job_from_db(id)
    applicant_name = request.form['full_name']
    gender = request.form['gender']
    explanation = request.form['additional_info']
    resume = request.form['resume_url']
    message = save_application_into_db(id, applicant_name, gender, explanation, resume)
    return render_template('job.html', page_title=job[1], job=job, message=message)

