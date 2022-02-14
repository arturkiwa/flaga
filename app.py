from flask import Flask, render_template
from genpass import createpassword, checkstrength

app=Flask(__name__)


@app.route('/')
def index():
    text = open("xd.txt").read()
    return render_template("index.html", text=text)


@app.route('/xd')
def flaga():
    text = open("flaga.txt").read()
    return render_template("flaga.html", text=text)


@app.route('/passwd')
def passwd():
    var1, var2 = createpassword()
    passwordstrength = checkstrength(var2)
    return render_template("passwd.html", passvar=var1, passwords=var2, strength=passwordstrength)


if __name__=="__main__":
    app.run(host="0.0.0.0")