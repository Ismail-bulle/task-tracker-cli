# Task Tracker CLI

A simple command-line task tracker built with Python.

This project was created as a Python learning project to practice working with command-line arguments, functions, lists, dictionaries, JSON files, and the filesystem.

## Features

* Add tasks
* Update tasks
* Delete tasks
* Mark tasks as in-progress
* Mark tasks as done
* List all tasks
* List completed tasks
* List pending tasks
* List tasks currently in progress
* Store tasks locally in a JSON file

## Technologies Used

* Python 3
* JSON
* Python standard library
* Command Line Interface (CLI)

No external libraries or frameworks are required.

## Project Structure

```text
task-tracker-cli/
│
├── task_tracker.py
├── README.md
└── .gitignore
```

The `tasks.json` file is created automatically when the application is used.

## How to Run

Clone the repository and open the project folder in your terminal.

Run:

```bash
python task_tracker.py
```

## Commands

### Add a task

```bash
python task_tracker.py add "Buy groceries"
```

### List all tasks

```bash
python task_tracker.py list
```

### Update a task

```bash
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_tracker.py delete 1
```

### Mark a task as in progress

```bash
python task_tracker.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_tracker.py mark-done 1
```

### List completed tasks

```bash
python task_tracker.py list done
```

### List pending tasks

```bash
python task_tracker.py list todo
```

### List tasks in progress

```bash
python task_tracker.py list in-progress
```

## Task Data

Each task contains:

* `id` — Unique task ID
* `description` — Task description
* `status` — `todo`, `in-progress`, or `done`
* `createdAt` — Date and time the task was created
* `updatedAt` — Date and time the task was last updated

## What I Learned

Through this project, I practiced:

* Python functions
* Lists and dictionaries
* Loops and conditional statements
* Command-line arguments using `sys.argv`
* Reading and writing files
* Working with JSON data
* Handling user input
* Working with timestamps
* Basic error handling
* Building a simple CLI application

## Future Improvements

Possible improvements for this project include:

* Add a task search feature
* Add task priorities
* Add due dates
* Add task categories
* Add a command to display task statistics
* Improve error handling
* Add automated tests

## Author

Built as part of my journey learning Python and developing my programming and cybersecurity skills.
