import sqlite3
from flask import Flask, render_template, request
import os
from werkzeug.utils import redirect
currentLocation = os.path.dirname(os.path.abspath(__file__))
myapp = Flask(__name__)
@myapp.route("/")
def homepage():
    return render_template("homepage.html")
@myapp.route("/",methods=["POST"])
def checklogin():
    UN=request.form['Username']
    PW = request.form['password']
    sqlconnection=sqlite3.connect(currentLocation +"login.db")
    cursar=sqlconnection.cursar()
    query1="SELECT username,password from users WHERE username={un} AND password ={pw}".format(un=UN,pw=PW)
    rows=cursar.execute(query1)
    rows=rows.fetchall()
    if len(rows)==1:
        return render_template("logged.html")
    else:
        return redirect("/register")
@myapp.route("/register",methods=["GET","POST"])
def registerpage():
    if request.method=="POST":
        dUN=request.form["Dusername"]
        dPW = request.form["Dpassword"]
        email=request.form["Emailuser"]
        sqlconnection=sqlite3.connection(currentLocation +"login.db")
        cursar=sqlconnection.cursar()
        query1="INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u=dUN,p=dPW,e=email)
        cursar.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("register.html")


if __name__=='__main__':
    myapp.run()