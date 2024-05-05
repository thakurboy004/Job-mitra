from sqlalchemy import create_engine, text
import os

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

# getting job from database
def get_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs WHERE id = :id"), {'id': id})
        job = result.fetchone()
    return job

# Storing the application into the database
def save_application_into_db(id, applicant_name, gender, explanation, resume):
    with engine.connect() as connection:
        connection.execute(text("INSERT INTO applications (`id`, `applicant_name`, `gender`, `explanation`, `resume_url`) VALUES (:id, :applicant_name, :gender, :explanation, :resume)"), {'id': id, 'applicant_name': applicant_name, 'gender':gender, 'explanation': explanation, 'resume': resume})
        connection.commit()
    return "Your application is under process. We will get back to you soon."



def load_jobs_from_db():
    # Assuming you have already created the engine object with the correct database URL
    # engine = create_engine('sqlite:///example.db', echo=True)  # Update with your database URL
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(row)  # Append the row directly, no need to convert to dictionary
        return jobs
