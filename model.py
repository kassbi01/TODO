from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    goal = db.Column(db.String(200))#, nullable=False)
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
        return str(self.priority) #<todo-list(goal='%s', priority='%s', date='%s', month='%s', complete='%s)>" % (self.goal, self.priority, self.date, self.month)
    
    def getInfo(self):
        return (str(self.goal),str(self.priority), str(self.date), str(self.month), str(self.complete))