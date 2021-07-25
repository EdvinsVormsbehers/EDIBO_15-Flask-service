from flask import Flask, render_template, jsonify, make_response, redirect, url_for, request
import pymysql

ufile = open('user.txt', 'r')
user = ufile.read() [:-1]
ufile.close()

pfile = open('password.txt', 'r')
password = pfile.read() [:-1]
pfile.close()

app = Flask(__name__)
db = pymysql.connect(host="localhost",
                     user=user,
                     password=password,
                     db="music_shop",
                     charset="utf8mb4",
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM users")
    show_users = cursor.fetchall()

    return render_template('index.html', users=show_users)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        Username = request.form['Username']
        Password = request.form['Password']
        cursor.execute("INSERT INTO users (EmployeeId, User_name, User_password, User) VALUES (%s, %s, %s, %s)", (1, Username, Password, 1))
        db.commit()
        return redirect(url_for('insert'))
    else:
        return render_template('user.html')

