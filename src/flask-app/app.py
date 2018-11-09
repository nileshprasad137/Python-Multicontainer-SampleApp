import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# Configure MySQL connection.
userpass = 'mysql+pymysql://root:root@db:3306/'
# db above is the name of the service
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
    app.run(host="127.0.0.1", port=80)