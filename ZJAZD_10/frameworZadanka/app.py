from framework import Framework

app = Framework()

@app.route('/example')
def example():
    print("hello worldd")

#####################################

# print(app.url_for('example'))

# for URL, fr in app.routes():
#     print(URL,fr)

#############################################

@app.route('/hello')
def hello():
    print("ala ma kocura")

#############################################

@app.route('/user/([a-zA-Z0-9-_]+)')
def user(who):
    print("user: ", who)

app.run()