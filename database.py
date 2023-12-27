import sqlite3

def creat(database_name = 'database.db'):
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE jobs 
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
def add_application_to_db(job_id ,application ):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS application(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   job_id INT not null,
                   full_name VARCHAR(250) NOT NULL,
                   email VARCHAR(250) NOT NULL,
                   linkedin_url VARCHAR(500)                   
    )""")
    conn.commit()
    conn.close()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""insert into application(
                   job_id, full_name, email, linkedin_url) values(?,?,?,?)""",
                     (job_id['id'], application['full_name'], application['email'],
                       application['Linkedin']))
    

    conn.commit()
    conn.close()
