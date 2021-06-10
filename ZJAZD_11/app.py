from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/<username>')
def hello_world(username):
    # return 'Hello World! {username}'.format(username=username)
    # return f'Hello World! {username}'
    return render_template('template.html', name=username)

@app.route('/')
def new():
    # return redirect(url_for('uname', username='wpisz sobie co chcesz'))
    return redirect(url_for(hello_world.__name__, username='user'))

@app.route('/form',methods=("POST","GET"))
def form():
    if request.method == "POST":
        if request.form["name"]=="Tomi":
            return "ok"
        else:
            return "error"

    return render_template('form.html')


if __name__ == '__main__':
    app.run()