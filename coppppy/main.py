import sqlite3
from flask import Flask , render_template
def dataBase():
    try:
        db = sqlite3.connect("cv.db")
        cr = db.cursor()
        cr.execute("CREATE TABLE if not exists cv_skill (skill text  ,progress integer)")
        #cr.execute("""insert into  cv_skill values('html',70),('python',90),('Js',65),('sql',85)""")
        cr.execute("select * from cv_skill")
        my_skills=cr.fetchall()
        db.commit()
        db.close()
        return my_skills
    except sqlite3.Error as er:
        print(f"Error Reading Data {er}")

s=dataBase()
cv =Flask(__name__)
@cv.route("/")
def skills():
    return render_template("skill.html",
                           title="skills",
                           pageHead="Naira Galal",
                           description="This is my skills ",
                           skill=s)
if __name__ == "__main__":
    cv.run(debug=True,port=333)





