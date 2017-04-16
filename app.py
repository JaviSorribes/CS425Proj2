from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from datetime import date,timedelta
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
	'parent': ['parentid', 'lastname', 'firstname'],
	'parent_contact': ['parentid', 'contact'],
	'course': ['name', 'year', 'semester', 'teacherid'],
	'book': ['bookid', 'isbn', 'cost', 'duedate', 'datecheckedout', 'title', 'coursename', 'courseyear', 'coursesemester', 'studentid'],
	'book_request': ['requestid', 'isbn', 'cost', 'title', 'coursename', 'courseyear', 'coursesemester', 'requestedby', 'quantity'],
	'has': ['studentid', 'parentid'],
	'takes': ['studentid', 'name', 'year', 'semester'],
	'controls': ['adminid', 'bookid'] }
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
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allbooksstudentfees(studentid):
        query = "SELECT * FROM book WHERE book.studentid={} AND book.duedate<'{}'".format(studentid,date.today().isoformat())
        cursor.execute(query)
        book_schema = schemas['book']
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def allstudents(): #an example
        query = "SELECT * FROM student"
        cursor.execute(query)
        return [tup2dict(tup,'student') for tup in cursor.fetchall()]
    def bookTitles():   #Returns the titles for the searching of the books
        query = "SELECT * FROM book GROUP BY title"
        cursor.execute(query)
        #temp = [s for s in cursor.fetchall()]
        return [tup2dict(tup,'book') for tup in cursor.fetchall()]
    def groupBooks():
        query = "SELECT isbn, title, coursename, courseyear, coursesemester, COUNT(*) as quantity, cost FROM book GROUP BY isbn, coursename, courseyear, coursesemester ORDER BY coursename, courseyear, coursesemester"
        cursor.execute(query)
        book_Group = ['isbn', 'title', 'coursename', 'courseyear', 'coursesemester', 'quantity', 'cost']
        return [tup2dict(tup, book_Group) for tup in cursor.fetchall()]
<<<<<<< HEAD
    return dict(allbooks=allbooks, allbooksstudent=allbooksstudent, allbooksstudentavailable=allbooksstudentavailable, allstudents=allstudents, groupBooks=groupBooks,
                bookTitles=bookTitles)
=======
    def parentcontacts(studentid):
        query = "SELECT parent_contact.contact, parent_contact.lastname, parent_contact.firstname FROM parent_contact LEFT JOIN has ON parent_contact.lastname=has.lastname AND parent_contact.firstname=has.firstname WHERE studentid={}".format(studentid)
        cursor.execute(query)
        parent_contact_schema = schemas['parent_contact']
        return [tup2dict(tup,'parent_contact') for tup in cursor.fetchall()]
    def allrequests():
        query = "SELECT * FROM book_request"
        cursor.execute(query)
        return [tup2dict(tup, 'book_request') for tup in cursor.fetchall()]

    return dict(allbooks=allbooks, allbooksstudent=allbooksstudent, allbooksstudentavailable=allbooksstudentavailable, allbooksstudentfees=allbooksstudentfees, allstudents=allstudents, groupBooks=groupBooks, parentcontacts=parentcontacts, allrequests=allrequests)
>>>>>>> 71f794a79d803cd5e0280bc597c100f28768198f


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
            return render_template('admin.html', user=user, today=date.today())
        elif data['role'] == 2:
            query = "SELECT * FROM teacher WHERE teacherid = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'teacher')
            return render_template('teacher.html', user=user, today=date.today())
        else: #==3
            query = "SELECT * FROM student WHERE studentid = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'student')
            return render_template('student.html', user=user, today=date.today())
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

@app.route("/request_book_teacher")
def request_book_teacher():
    isbn = request.args["bookisbn"]
    course_name = request.args["coursename"]
    quantity = request.args["quantity"]
    course_year = request.args["courseyear"]
    course_sem = request.args["coursesem"]
    methodcalls.book_all(isbn)
    cost = methodcalls.book_price(isbn)
    if cost == "error":
        print("error")
    title = methodcalls.book_title(isbn)

    query = "INSERT INTO book_request (isbn,cost,title,coursename,courseyear,coursesemester,requestedby,quantity) " \
    "VALUES ({},{},\"{}\",\"{}\",\"{}\",\"{}\",'teacher',{});".format(isbn,cost,title,course_name,course_year,course_sem,quantity)
    cursor.execute(query)
    conn.commit()
    return render_template("teacher-requestdone.html")

@app.route("/book_info/<isbn>")
def book_info(isbn):
    book_isbn = isbn
    #methodcalls.book_summary("0439708184")
    information = methodcalls.book_all(isbn)
    print(information)
    return render_template('admin-bookinfo.html', user=user, information=information)

@app.route("/borrow_book/<studentid>/<bookid>")
def borrow_book(studentid, bookid):
    query = "SELECT * FROM book WHERE bookid={}".format(bookid)
    cursor.execute(query)
    answer = [tup2dict(tup, 'book') for tup in cursor.fetchall()]
    answer = answer[0]
    query="UPDATE book SET studentid={}, datecheckedout='{}', duedate=DATE_ADD(datecheckedout, INTERVAL 30 DAY) WHERE bookid={}".format(studentid, date.today().isoformat(), bookid)
    cursor.execute(query)
    conn.commit()
    return render_template('student.html', user=user, today=date.today())

@app.route("/grant_request/<requestid>")
def book_request_grant(requestid):
    query = "SELECT * FROM book_request WHERE requestid = {}".format(requestid)
    cursor.execute(query)
    answer = [tup2dict(tup, 'book_request') for tup in cursor.fetchall()]
    answer = answer[0]
    # This stuff removes the book from request
    query = "DELETE FROM book_request WHERE requestid = {}".format(requestid)
    cursor.execute(query)
    conn.commit()
    # First we have to insert the course into course.
    query = "INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester) VALUES ({},{},\'{}\',\'{}\',{},\'{}\')".format(answer["isbn"],answer["cost"],answer["title"],answer["coursename"],answer["courseyear"],answer["coursesemester"])
    #print(query)
    cursor.execute(query)
    conn.commit()
    return render_template('admin.html', user=user)

@app.route("/borrow_book/<bookid>")
def return_book(bookid):
    query = "SELECT * FROM book WHERE bookid={}".format(bookid)
    cursor.execute(query)
    answer = [tup2dict(tup, 'book') for tup in cursor.fetchall()]
    answer = answer[0]
    query="UPDATE book SET studentid=NULL, datecheckedout=NULL, duedate=NULL WHERE bookid={}".format(bookid)
    cursor.execute(query)
    conn.commit()
    return render_template('student.html', user=user, today=date.today())

@app.route("/") #asking the user for dates
def index():
    global user
    user = None # reset it when going to login
    return render_template('login.html')

if __name__ == '__main__':
    app.run()