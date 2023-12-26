import sqlite3
from flask import  Flask ,render_template , jsonify
from database import load_jobs_from_db
app = Flask(__name__)


@app.route('/')
def hello_world():
    JOBS = load_jobs_from_db()
    return render_template( 'home.html' , jobs = JOBS)
@app.route('/jobs')
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug = True)
    # 