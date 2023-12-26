import sqlite3
from flask import  Flask ,render_template , jsonify
from database import load_jobs_from_db
app = Flask(__name__)


@app.route('/')
def hello_world():
    JOBS = load_jobs_from_db()
    return render_template( 'home.html' , jobs = JOBS)
@app.route('/api/jobs')
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)

@app.route('/jobs/<id>')
def show_jobs(id):
    JOBS = load_jobs_from_db()
    select_job = None
    for job in JOBS:
        if job['id'] == int(id):
            select_job = job
    return select_job

if __name__ == "__main__":
    app.run(debug = True)
    # 