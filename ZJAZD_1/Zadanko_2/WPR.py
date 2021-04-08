#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example', methods=('GET','POST'))
def example():
    lhs=float(request.form['firstNumber'])
    rhs=float(request.form['secondNumber'])
    opr=(request.form['sing'])
    result=0
    if(opr=='+'):
        result=lhs+rhs
    elif(opr=='-'):
        result=lhs-rhs
    elif(opr=='*'):
        result=lhs*rhs
    elif(opr=='/'):
        result=lhs/rhs
    return str(result)

if __name__=='__main__':
    app.run(debug=True)