from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import methodcalls

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
user = None

# Our database's schemas
schemas = { 'user': ['username', 'userpass', 'role', 'id'],
	'admin': ['adminid', 'lastname', 'firstname'],
	'teacher': ['teacherid', 'lastname', 'firstname'],
	'student': ['studentid', 'firstname', 'lastname', 'amountdue', 'advisorid'],
	'parent': ['lastname', 'firstname'],
	'parent_contact': ['contact', 'lastname', 'firstname'],
	'course': ['name', 'year', 'semester', 'teacherid'],
	'book': ['bookid', 'isbn', 'cost', 'duedate', 'datecheckedout', 'title', 'coursename', 'courseyear', 'coursesemester', 'studentid'],
	'book_request': ['requestid', 'isbn', 'cost', 'title', 'coursename', 'courseyear', 'coursesemester', 'requestedby', 'quantity'],
	'has': ['studentid', 'lastname', 'firstname'],
	'takes': ['studentid', 'name', 'year', 'semester'],
	'controls': ['adminid', 'bookid'],
    'book_Group': ['isbn','title','coursename','courseyear','coursesemester','quantity','cost']}
# Take tuple, create dictionary:
def tup2dict(tup,schema): #assumes right arguments
    if isinstance(schema,str): #allows you to give the name of one of the default schemas
        schema = schemas[schema]    #else, we will just use the schema list that you give us!
    if not tup or len(tup) != len(schema): #no tuple, or mismatch with schema
        return None
    return {schema[i]:tup[i] for i in range(len(schema))}

### SQL COMMANDS to be called dynamically from the templates: ###
@app.context_processor
def sqlcommands():
    #define as many commands as needed here, and add them to the dict returned
    def groupBooks():
        query = "SELECT isbn, title, coursename, courseyear, coursesemester, COUNT(*) as quantity, cost FROM book GROUP BY isbn, coursename, courseyear, coursesemester ORDER BY coursename, courseyear, coursesemester"
        cursor.execute(query)
        return [tup2dict(tup,'book_Group') for tup in cursor.fetchall()]
    def allbooks():
        query = "SELECT * FROM book"
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allbooksstudent(studentid):
        query = "SELECT * FROM book WHERE book.studentid={}".format(studentid)
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allbooksstudentavailable(studentid):
        query = "SELECT DISTINCT book.bookid, book.isbn, book.cost, book.duedate, book.datecheckedout, book.title, book.coursename, book.courseyear, book.coursesemester, book.studentid FROM (SELECT takes.name, takes.year, takes.semester FROM student RIGHT JOIN takes ON student.studentid=takes.studentid WHERE student.studentid={}) AS dtable RIGHT JOIN book ON book.coursename=dtable.name AND book.courseyear=dtable.year AND book.coursesemester=dtable.semester WHERE book.studentid is null AND dtable.name is not null".format(studentid)
        #query = "SELECT * FROM book WHERE book.studentid is null"
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allstudents(): #an example
        query = "SELECT * FROM student"
        cursor.execute(query)
        return [tup2dict(tup,'student') for tup in cursor.fetchall()]
<<<<<<< HEAD
    return dict(allbooks=allbooks, allstudents=allstudents, groupBooks=groupBooks)
=======
    return dict(allbooks=allbooks, allbooksstudent=allbooksstudent, allbooksstudentavailable=allbooksstudentavailable, allstudents=allstudents)
>>>>>>> c61b9bbdc9b411044c8ed43db8a727de80b023a8


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

# NEED THE REMOVE THE FUNCTION. IT'S IMPORTANT!!!
@app.route("/books")
def books():
    if request.args['bookname'].lower() == "all books":
        query = "SELECT * FROM book"
        cursor.execute(query)
        books = [tup2dict(tup,'book') for tup in cursor.fetchall()]
        return render_template('admin-book.html', books = books, user = user)
    query = "SELECT * FROM book WHERE title = \"{}\"".format(request.args['bookname'])
    cursor.execute(query)
    books = [tup2dict(tup,'book') for tup in cursor.fetchall()]
    print(books)
    if books:
        return render_template('admin-book.html',books=books, user=user)
    else:
        return render_template('admin-bookerror.html',user=user)

@app.route("/book_info/<isbn>")
def book_info(isbn):
    book_isbn = isbn
    #methodcalls.book_summary("0439708184")
    information = methodcalls.book_all(isbn)
    print(information)
    return render_template('admin-bookinfo.html', user=user, information=information)

@app.route("/") #asking the user for dates
def index():
    global user
    user = None # reset it when going to login
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
