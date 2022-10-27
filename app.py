from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
    name = db.Column('student_id', db.Integer, primary_key = True)
    phone_no = db.Column(db.String(100))
    address = db.Column(db.String(50))

def __init__(self, name, phone_no, address):
    self.name = name
    self.phone_no = phone_no
    self.address


# Name, Phone No, Address
# Add, View, Delete, Reset

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all() )

if __name__ == '__main__':
    #db.create_all()
    app.run(debug = True)
