# Flask To-Do List

A simple to-do list web application built with Flask and SQLite.

## Features
- Add, complete, and delete tasks
- Tasks are stored in a local SQLite database
- Responsive UI with Bootstrap

## Project Structure
```
to_do_list/
│   app.py
│   db.sqlite3
│
├───static/
│   └───css/
│           style.css
│
├───templates/
│       index.html
```

## Setup Instructions

### 1. Clone the repository or copy the project files

### 2. Install dependencies
Make sure you have Python 3 installed. Then, install Flask:

```
pip install flask
```

### 3. Run the application

From the `to_do_list` directory, run:

```
python app.py
```

The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 4. Usage
- Add a new task using the input field and "Add Task" button.
- Mark a task as complete with the "Complete" button.
- Delete a task with the "Delete" button.

## Notes
- The database file (`db.sqlite3`) is created automatically in the project root.
- If you encounter a `no such table: tasks` error, ensure you are running the app from the correct directory and that the `init_db()` function is called.

## License
This project is for educational purposes.
