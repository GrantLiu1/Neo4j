from flask import *
app=Flask(__name__)

@app.route('/hello')
def hello():
    return "hello Flask"

@app.route('/rend')
def rend():
    name = "liu"
    users = ["Grant", "Henry", "lana"]
    return render_template("index.html", name=name, users=users)

if  __name__  ==  '__main__':
    app.run()