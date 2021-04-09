#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
USERS = [
    ("Fidur",1),
    ("Dareczek",2),
    ("Krystianek",3),
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<int:user_id>')
def users(user_id):
    x=[x for x in USERS if x[1]==user_id]
    if(x):
        return str(x[0])
    else:
        return "Nie ma takiego użytkownika"

if __name__=='__main__':
    app.run(debug=True)