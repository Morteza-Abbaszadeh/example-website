import sqlite3

def creat(database_name = 'database.db'):
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE jobs 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(250) NOT NULL,
                location VARCHAR(250) NOT NULL,
                salary INT NOT NULL,
                currency VARCHAR(10),
                responsibilities VARCHAR(2500),
                requirements VARCHAR(2500))''')
    conn.commit()
    conn.close()

def  insert(title ,location, salary  , currency=None , responsibilities=None ,requirements=None ):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, location, salary, currency, responsibilities, requirements))

    conn.commit()
    conn.close()
def load_jobs_from_db():
    conn = sqlite3.connect('database.db')
    c =  conn.execute('select * from jobs')

    jobs = []
    columns_name = []
    for col in c.description:
        columns_name.append(col[0] )

    for row in c.fetchall():
        job_dict = dict(zip(columns_name, row))
        jobs.append(job_dict)
    return jobs 