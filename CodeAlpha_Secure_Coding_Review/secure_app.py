from flask import Flask, request
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT password FROM users WHERE username=?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and check_password_hash(result[0], password):
        return "Login successful"
    else:
        return "Invalid credentials"

app.run(debug=False)