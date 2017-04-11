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
    conn = mysql.connect()
    cursor =conn.cursor()
    query = "SELECT * FROM user WHERE username = \"{}\" AND userpass = \"{}\"".format(username,password)
    #print(query)
    cursor.execute(query)
    data = cursor.fetchone()
    if data:
        print(data[2])
        if data[2] == 3:
            return render_template('student.html')
        elif data[2] == 2:
            return render_template('teacher.html')
        else: #==1
            return render_template('admin.html')

    #USER DOESN'T EXIST SO JUST DISPLAY SAME PAGE AGAIN
    return render_template('error.html')


@app.route("/") #asking the user for dates
def index():
    #conn = mysql.connect()
    #cursor =conn.cursor()
    #cursor.execute("SELECT * from users")
    #data = cursor.fetchone()
    #print(data)
    #print('kkkkk')
    #for c in cursor:
        #print(c)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
