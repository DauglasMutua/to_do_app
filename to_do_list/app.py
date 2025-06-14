from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '../db.sqlite3')

#initialize the database
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     task TEXT NOT NULL, 
                     completed INTEGER DEFAULT 0
                     )''')
    conn.close()

#home route
@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

#add a task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    return redirect(url_for('index'))

#mark a task as completed
@app.route('/complete/<int:id>')    
def complete_task(id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE tasks SET completed=1 WHERE id=?", (id,))
    return redirect(url_for('index'))

#delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM tasks WHERE id= ?", (id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
