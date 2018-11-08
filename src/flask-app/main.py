from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

userpass = 'mysql+pymysql://root:root@localhost:3306/'
dbname   = 'multicontainer_todoapp'

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + dbname
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todoItem = db.Column(db.String(80))

    def __init__(self, todoItem):
        self.todoItem = todoItem


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/todo", methods=["GET"])
def view_todos():
    all_todos = Todo.query.all()
    return render_template('todoList.html', todos=all_todos)

@app.route("/todo/create", methods=["POST"])
def create_note():    
    todoItem = request.form["todoItem"]

    todo = Todo(todoItem=todoItem)

    db.session.add(todo)
    db.session.commit()

    return redirect("/todo")

if __name__ == "__main__":
    app.run(debug=True)