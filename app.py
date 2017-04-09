from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/") #asking the user for dates
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
