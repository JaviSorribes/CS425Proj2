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
conn = mysql.connect()
cursor =conn.cursor()

# Global user once logged-in
user = {}

# Our database's schemas
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

# Take tuple, create dictionary:
def tup2dict(tup,schema_name): #assumes right arguments
    schema = schemas[schema_name]
    return {schema[i]:tup[i] for i in range(len(schema))}

### SQL COMMANDS to be called dynamically from the templates: ###
@app.context_processor
def sqlcommands():
    #define as many commands as needed here, and add them to the dict returned
    def allbooks():
        query = "SELECT * FROM book"
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allstudents(): #an example
        query = "SELECT * FROM student"
        cursor.execute(query)
        return [tup2dict(tup,'student') for tup in cursor.fetchall()]
    return dict(allbooks=allbooks, allstudents=allstudents)

### PAGES (ROUTES): ###
@app.route("/home", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM user WHERE username = \"{}\" AND userpass = \"{}\"".format(username,password)
    cursor.execute(query)
    data = tup2dict(cursor.fetchone(),'user')
    if data:
        global user #to reference the global user guy
        if data['role'] == 1:
            query = "SELECT * FROM admin WHERE adminid = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'admin')
            return render_template('admin.html', user=user)
        elif data['role'] == 2:
            query = "SELECT * FROM teacher WHERE teacherid = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'teacher')
            return render_template('teacher.html', user=user)
        else: #==3
            query = "SELECT * FROM student WHERE studentid = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'student')
            return render_template('student.html', user=user)
    #USER DOESN'T EXIST SO JUST DISPLAY SAME PAGE AGAIN
    return render_template('error.html')

@app.route("/books")
def books():
    query = "SELECT * FROM book WHERE title = {}".format(request.args['bookname'])
    cursor.execute(query)
    books = [tup2dict(tup,'book') for tup in cursor.fetchone()]
    return render_template('admin-book.html',books=books)

@app.route("/") #asking the user for dates
def index():
    global user
    user = {} # reset it when going to login
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
