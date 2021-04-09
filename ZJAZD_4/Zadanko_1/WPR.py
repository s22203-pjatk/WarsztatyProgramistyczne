#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator/<string:op>/<float:lhs>/<float:rhs>', methods=('GET','POST'))
def calculator(op,lhs,rhs):
    result=0
    if (op == '+'):
        result = lhs + rhs
    elif (op == '-'):
        result = lhs - rhs
    elif (op == '*'):
        result = lhs * rhs
    elif (op == ';'):
        result = lhs / rhs
    return str(result)

if __name__=='__main__':
    app.run(debug=True)