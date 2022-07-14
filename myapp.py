import sqlite3
from flask import Flask, render_template, request
from werkzeug.utils import redirect

login_app = Flask(__name__)
db=sqlite3.connect("login.db")
@login_app.route("/")
def homepage():
    return render_template("homepage.html")
@login_app.route("/",methods=["POST"])
def checklogin():
    UN=request.form['Username']
    PW = request.form['password']
    query1="SELECT username,password from users WHERE username={un} AND password ={pw}".format(un=UN,pw=PW)
    rows =db.execute(query1)
    rows = rows.fetchall()
    if len(rows)==1:
        #return render_template("logged.html")
        return "L"
    else:
        #return redirect("register.html")
        return "R"

@login_app.route("/register",methods=["GET","POST"])
def registerpage():
    if request.method=="POST":
        dUN=request.form["Dusername"]
        dPW = request.form["Dpassword"]
        email=request.form["Emailuser"]
        query1="INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u=dUN,p=dPW,e=email)
        db.execute(query1)
        db.commit()
        #return redirect("/")
        return  "H"
    #return render_template("register.html")
    return "R"






if __name__=='__main__':
    login_app.run()