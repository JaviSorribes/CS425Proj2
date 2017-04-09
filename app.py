from flask import Flask, request, render_template
from flask.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'library'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/") #asking the user for dates
def index():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from User")
    data = cursor.fetchone()
    print(data)
    print('kkkkk')
    for c in cursor:
        print(c)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
