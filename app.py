from flask import  Flask ,render_template , jsonify ,request
from database import load_jobs_from_db,add_application_to_db

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
            print(select_job)
    if select_job == None:
        return "Not Found" , 404
    else :
        return render_template('jobpage.html' ,job= select_job)
@app.route("/jobs/<id>/apply", methods = ['post'] )
def apply_to_job(id):
    data = request.form
    JOBS = load_jobs_from_db()
    select_job = None
    for job in JOBS:
        if job['id'] == int(id):
            select_job = job
    add_application_to_db(select_job,data)
    return render_template('app_submit.html' , application = data,job= select_job)

if __name__ == "__main__":
    app.run(debug = True)
    # 