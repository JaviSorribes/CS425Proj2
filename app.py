from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'library'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

#our database's schemas
schemas = { 'user': ['username', 'userpass', 'role', 'id'],
	'admin': ['adminid', 'lastname', 'firstname'],
	'teacher': ['teacherid', 'lastname', 'firstname'],
	'student': ['studentid', 'firstname', 'lastname', 'amountdue', 'advisorid'],
	'parent': ['lastname', 'firstname'],
	'parent_contact': ['contact', 'lastname', 'firstname'],
	'course': ['name', 'year', 'semester', 'teacherid'],
	'book': ['bookid', 'isbn', 'cost', 'duedate', 'datecheckedout', 'orderbytype', 'title', 'coursename', 'courseyear', 'coursesemester', 'studentid'],
	'has': ['studentid', 'lastname', 'firstname'],
	'takes': ['studentid', 'name', 'year', 'semester'],
	'controls': ['adminid', 'bookid'] }

### SQL COMMANDS to be called dynamically from the templates: ###
@app.context_processor
def sqlcommands():
    #define as many commands as needed here, and add them to the dict returned
    def allstudents(): #an example
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM student"
        cursor.execute(query)
        student_schema = schemas['student']
        return [{student_schema[i]:tup[i] for i in range(len(student_schema))} for tup in cursor.fetchall()]
    return dict(allstudents=allstudents)

### PAGES (ROUTES): ###
#schema user: (username, password, access, fk_id). PK: (username,password)
@app.route("/home", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connect()
    cursor =conn.cursor()
    query = "SELECT * FROM user WHERE username = \"{}\" AND userpass = \"{}\"".format(username,password)
    cursor.execute(query)
    data = cursor.fetchone()
    if data:
        print(data[2])
        if data[2] == 1:
            query = "SELECT * FROM admin WHERE adminid = {}".format(data[3])
            cursor.execute(query)
            return render_template('admin.html', user=cursor.fetchone())
        elif data[2] == 2:
            query = "SELECT * FROM teacher WHERE teacherid = {}".format(data[3])
            cursor.execute(query)
            return render_template('teacher.html', user=cursor.fetchone())
        else: #==3
            query = "SELECT * FROM student WHERE studentid = {}".format(data[3])
            cursor.execute(query)
            return render_template('student.html', user=cursor.fetchone())

    #USER DOESN'T EXIST SO JUST DISPLAY SAME PAGE AGAIN
    return render_template('error.html')

@app.route("/") #asking the user for dates
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
