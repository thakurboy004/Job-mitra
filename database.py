from sqlalchemy import create_engine, text
import os
from .env import SQL_URL

engine = create_engine(os.getenv('DATABASE_URL'))

# getting jobs from database
def get_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs WHERE id = :id"), {'id': id})
        job = result.fetchone()
    return job

# Storing the application into the database
def save_application_into_db(id, applicant_name, gender, explanation, resume):
    with engine.connect() as connection:
        connection.execute(text("INSERT INTO applications (id, applicant_name, gender, explanation, resume) VALUES (:id, :applicant_name, :gender, :explanation, :resume)"), {'id': id, 'applicant_name': applicant_name, 'gender':gender, 'explanation': explanation, 'resume': resume})
    return "Your application is under process. We will get back to you soon."

print(SQL_URL)