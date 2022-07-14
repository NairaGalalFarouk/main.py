from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
FLASK_APP =Flask(__name__)
FLASK_APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
FLASK_APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(FLASK_APP)
class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@FLASK_APP.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = task.query.order_by(task.date_created).all()
        return render_template('index.html', tasks=tasks)

@FLASK_APP.route('/delete/<int:id>')
def delete(id):
    task_to_delete = task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
@FLASK_APP.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    t = task.query.get_or_404(id)
    if request.method == 'POST':
        t.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)









if __name__ == "__main__":
    FLASK_APP.run(debug=True,port=181)