from flask import Flask, render_template,request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    goal = db.Column(db.String(200))
    priority = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    complete = db.Column(db.Boolean)

    

    def __init__(self, goal, priority, date, month, complete):
        self.goal = goal
        self.priority = priority
        self.date = date
        self.month = month
        self.complete = False
    
    def __repr__(self):
        return str(self.complete)

    def getInfo(self):
        return (str(self.id), str(self.goal),str(self.priority), str(self.date), str(self.month), str(self.complete))

@app.route('/', methods = ['POST','GET'])
def index():
    return render_template('index.html')

def get_input():
    return [request.form.get('goal'), request.form.get('priority'), request.form.get('day'), request.form.get('month')]
     

def the_database():
    input_data = get_input()
    return Todo(input_data[0], input_data[1], input_data[2], input_data[3], True)

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Home':
            if get_input()[0] != '':
                data = the_database()
                db.session.add(data)
                db.session.commit()
        
        if request.form['submit_button'] == 'Add to list':
            if get_input()[0] != '':
                data = the_database()
                db.session.add(data)
                db.session.commit()

    todos = Todo.query.filter_by(complete=False)
    goo = [i.getInfo() for i in todos]

    completes = Todo.query.filter_by(complete=True)
    done = [i.getInfo() for i in completes]
    return render_template("home.html", todos = goo, completes = done)


@app.route('/complete/<id>')
def save_it_as_completed(id):
    data = Todo.query.filter_by(id=int(id))[0]
    data.complete = True
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/incomplete/<id>')
def save_it_as_incompleted(id):
    data = Todo.query.filter_by(id=int(id))[0]
    data.complete = False
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()