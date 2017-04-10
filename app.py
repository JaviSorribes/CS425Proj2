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

#schema user: (username, password, access, fk_id). PK: (username,password)
@app.route("/login")
def login():
    username = request.args['username']
    password = request.args['password']
    print(username)
    print(password)
    '''
    conn = mysql.connect()
    cursor =conn.cursor()
    query = "SELECT * FROM user WHERE username = {} AND password = {}".format(username,password)
    cursor.execute(query)
    data = cursor.fetchone()
    '''
    if username == 'student':
        return render_template('student.html')
    elif username == 'teacher':
        return render_template('teacher.html')
    else:
        return render_template('admin.html')


@app.route("/") #asking the user for dates
def index():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from admin")
    data = cursor.fetchone()
    print(data)
    print('kkkkk')
    for c in cursor:
        print(c)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
