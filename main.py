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

