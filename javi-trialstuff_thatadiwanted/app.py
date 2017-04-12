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
@app.route("/")
def login():
    return render_template("trial.html")

@app.context_processor
def sqlcommands():
    def allstudents():
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM student"
        cursor.execute(query)
        schema = ['username','studentid','name','lastname','amountdue','advisorid']
        return [{schema[i]:tup[i] for i in range(len(schema))} for tup in cursor.fetchall()]
    return dict(allstudents=allstudents)

if __name__ == '__main__':
    app.run()
