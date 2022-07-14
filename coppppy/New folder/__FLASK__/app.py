from flask import Flask,render_template
import jinja2
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
app=Flask(__name__)
@app.route('/')
def index ():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)