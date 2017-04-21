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
    class allmethods:
        #define as many commands as needed here (in alphabetical order)
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
            #query = "SELECT DISTINCT book.bookid, book.isbn, book.cost, book.duedate, book.datecheckedout, book.title, book.coursename, book.courseyear, book.coursesemester, book.studentid FROM (SELECT takes.name, takes.year, takes.semester FROM student RIGHT JOIN takes ON student.studentid=takes.studentid WHERE student.studentid={}) AS dtable RIGHT JOIN book ON book.coursename=dtable.name AND book.courseyear=dtable.year AND book.coursesemester=dtable.semester WHERE book.studentid is null AND dtable.name is not null".format(studentid)
            query = "SELECT dt2.bookid, dt2.isbn, dt2.cost, dt2.duedate, dt2.datecheckedout, dt2.title, dt2.coursename, dt2.courseyear, dt2.coursesemester, dt2.studentid FROM (SELECT book.bookid, book.isbn, book.cost, book.duedate, book.datecheckedout, book.title, book.coursename, book.courseyear, book.coursesemester, book.studentid FROM book RIGHT JOIN (SELECT * FROM takes WHERE studentid={}) AS dt1 ON book.coursename=dt1.name AND book.courseyear=dt1.year AND book.coursesemester=dt1.semester WHERE book.studentid IS NULL) AS dt2 LEFT JOIN (SELECT * from book where studentid={}) AS dt3 ON dt2.coursename=dt3.coursename AND dt2.courseyear=dt2.courseyear AND dt2.coursesemester=dt3.coursesemester WHERE dt3.bookid IS NULL ORDER BY dt2.coursename, dt2.courseyear, dt2.coursesemester".format(studentid,studentid)

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
        def allrequests():
            query = "SELECT * FROM book_request"
            cursor.execute(query)
            return [tup2dict(tup, 'book_request') for tup in cursor.fetchall()]
        def allusers():
            query = "(SELECT studentid AS id,firstname,lastname,'student' AS access_level FROM student) UNION (SELECT teacherid AS id,firstname,lastname,'teacher' AS access_level FROM teacher) UNION (SELECT adminid AS id,firstname,lastname,'admin' AS access_level FROM admin);"
            cursor.execute(query)
            user_group = ['id','firstname','lastname','access_level']
            return [tup2dict(tup,user_group) for tup in cursor.fetchall()]
        def availableBooks():   #Returns data on the availability of all the books
            query = "select COUNT(*) AS total_num_books, COUNT(datecheckedout) AS total_checked_out, COUNT(*)-COUNT(datecheckedout) AS available FROM book;"
            cursor.execute(query)
            return cursor.fetchone()
        def bookTitles():   #Returns the titles for the searching of the books
            query = "SELECT * FROM book GROUP BY title"
            cursor.execute(query)
            #temp = [s for s in cursor.fetchall()]
            return [tup2dict(tup,'book') for tup in cursor.fetchall()]

        def courses():
            query = "SELECT DISTINCT(name) from COURSE"
            cursor.execute(query)
            course_schema = ['name']
            return [tup2dict(tup, course_schema) for tup in cursor.fetchall()]

        def findadvisor(advisorid):
            query = "SELECT * FROM teacher WHERE teacherid={}".format(advisorid)
            cursor.execute(query)
            return [tup2dict(tup,'teacher') for tup in cursor.fetchall()]

        def groupBooks():
            query = "SELECT isbn, title, coursename, courseyear, coursesemester, COUNT(*) as quantity, cost FROM book GROUP BY isbn, coursename, courseyear, coursesemester ORDER BY coursename, courseyear, coursesemester"
            cursor.execute(query)
            book_Group = ['isbn', 'title', 'coursename', 'courseyear', 'coursesemester', 'quantity', 'cost']
            return [tup2dict(tup, book_Group) for tup in cursor.fetchall()]

        def numbooksoverdue(studentid):
            query = "SELECT COUNT(*) FROM book WHERE studentid={}".format(studentid)
            cursor.execute(query)
            return cursor.fetchone()[0]

        def parentcontacts(studentid):
            query = "SELECT parent.lastname, parent.firstname, parent_contact.contact FROM has LEFT JOIN parent ON has.parentid=parent.parentid LEFT JOIN parent_contact ON parent.parentid=parent_contact.parentid WHERE studentid={}".format(studentid)
            cursor.execute(query)
            parentdisplay_schema = ['lastname', 'firstname', 'contact']
            return [tup2dict(tup, parentdisplay_schema) for tup in cursor.fetchall()]
        def semester():
            query = "SELECT DISTINCT(semester) from COURSE"
            cursor.execute(query)
            course_schema = ['semester']
            return [tup2dict(tup, course_schema) for tup in cursor.fetchall()]

        def year():
            query = "SELECT DISTINCT(year) from COURSE"
            cursor.execute(query)
            course_schema = ['year']
            return [tup2dict(tup, course_schema) for tup in cursor.fetchall()]

    ## Doing this instead avoids merge conflicts, since we don't have to change that line (DO NOT TOUCH)
    _forbidden_names = set(['__weakref__', '__module__', '__dict__', '__doc__'])
    return {k:v for k,v in allmethods.__dict__.items() if k not in _forbidden_names}
    #return dict(allbooks=allbooks, allbooksstudent=allbooksstudent, allbooksstudentavailable=allbooksstudentavailable,
     #           allbooksstudentfees=allbooksstudentfees, allstudents=allstudents, findadvisor=findadvisor, groupBooks=groupBooks,
      #          numbooksoverdue=numbooksoverdue,parentcontacts=parentcontacts, allrequests=allrequests, bookTitles = bookTitles,
       #         courses = courses,year=year, semester=semester, availableBooks=availableBooks, allusers=allusers)

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

@app.route("/request_book_student")
def request_book_student():
    course_name = request.args["coursename"]
    course_year = request.args["courseyear"]
    course_sem = request.args["coursesem"]
    query = "SELECT * FROM course WHERE name = \"{}\" and year = {} and semester = \"{}\"".format(course_name,course_year,course_sem)
    cursor.execute(query)
    result_dic = [tup2dict(tup, schemas["course"]) for tup in cursor.fetchall()]
    if result_dic:
        #print("success")

        query = "SELECT * FROM book WHERE coursename = \"{}\" and courseyear = {} and coursesemester = \"{}\"".format(course_name,course_year,course_sem)
        cursor.execute(query)
        result_dic = [tup2dict(cursor.fetchone(), schemas["book"]) ]
        isbn = result_dic[0]["isbn"]
        methodcalls.book_all(isbn)
        cost = methodcalls.book_price(isbn)
        if cost == "error":
            print("error")
        title = methodcalls.book_title(isbn)
        query = "INSERT INTO book_request (isbn,cost,title,coursename,courseyear,coursesemester,requestedby,quantity) " \
                "VALUES ({},{},\"{}\",\"{}\",\"{}\",\"{}\",'student',1);".format(isbn, cost, title, course_name,
                                                                                  course_year, course_sem )
        cursor.execute(query)
        conn.commit()
        return render_template("student-requestdone.html",user=user, today=date.today())
    else:
        print("error")
        return render_template("student-requesterror.html", user=user, today=date.today())

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

@app.route("/remove_user/<id>/<access_level>")
def remove_user(id,access_level):
    query= "SELECT * FROM {} WHERE {}id={}".format(access_level,access_level,id)
    cursor.execute(query)
    if access_level == 'student':
        answer = [tup2dict(tup, 'student') for tup in cursor.fetchall()]
    elif access_level == 'teacher':
        answer = [tup2dict(tup, 'teacher') for tup in cursor.fetchall()]
    else:
        answer = [tup2dict(tup, 'admin') for tup in cursor.fetchall()]
    answer = answer[0]
    query = "DELETE FROM {} WHERE {}id = {}".format(access_level,access_level,id)
    cursor.execute(query)
    conn.commit()
    return render_template('admin.html', user=user, today=date.today())

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
    updateamountdue()
    return render_template('login.html')

#update amounts due in students
def updateamountdue():
    query = "SELECT * FROM book WHERE duedate IS NOT NULL"
    cursor.execute(query)
    checkedout = [tup2dict(x, 'book') for x in cursor.fetchall()]
    query = "SELECT studentid FROM student"
    cursor.execute(query)
    studs={tup[0]:0 for tup in cursor.fetchall()}
    for b in checkedout:
        if b['duedate'] < date.today():
            studs[b['studentid']] += b['cost']
    for studid in studs:
        query = "UPDATE student SET amountdue = {} WHERE studentid={}".format(studs[studid],studid)
        cursor.execute(query)
        conn.commit()
    query = "SELECT studentid,amountdue FROM student"
    cursor.execute(query)

if __name__ == '__main__':
    app.run()
