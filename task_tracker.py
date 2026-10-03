import json
import sys
from datetime import datetime
import os


FILE_NAME = "tasks.json"


# Get the current date and time
def get_time():
    return datetime.now().isoformat()


# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Find a task by its ID
def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


# Add a new task
def add_task(description):
    tasks = load_tasks()

    # Create a new ID
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    now = get_time()

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


# Update a task
def update_task(task_id, description):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["description"] = description
    task["updatedAt"] = get_time()

    save_tasks(tasks)

    print("Task updated successfully.")


# Delete a task
def delete_task(task_id):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    tasks.remove(task)

    save_tasks(tasks)

    print("Task deleted successfully.")


# Change task status
def change_status(task_id, status):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["status"] = status
    task["updatedAt"] = get_time()

    save_tasks(tasks)

    print(f"Task marked as {status}.")


# List tasks
def list_tasks(status=None):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:

        if status is None or task["status"] == status:
            print(
                f'{task["id"]}. '
                f'{task["description"]} '
                f'[{task["status"]}]'
            )


# Main program
def main():

    if len(sys.argv) < 2:
        print("Please enter a command.")
        return

    command = sys.argv[1]

    # ADD
    if command == "add":

        if len(sys.argv) < 3:
            print("Please provide a task description.")
            return

        description = sys.argv[2]

        add_task(description)

    # UPDATE
    elif command == "update":

        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py update ID \"description\"")
            return

        task_id = int(sys.argv[2])
        description = sys.argv[3]

        update_task(task_id, description)

    # DELETE
    elif command == "delete":

        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            return

        task_id = int(sys.argv[2])

        delete_task(task_id)

    # MARK IN PROGRESS
    elif command == "mark-in-progress":

        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            return

        task_id = int(sys.argv[2])

        change_status(task_id, "in-progress")

    # MARK DONE
    elif command == "mark-done":

        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            return

        task_id = int(sys.argv[2])

        change_status(task_id, "done")

    # LIST
    elif command == "list":

        if len(sys.argv) == 2:
            list_tasks()

        else:
            status = sys.argv[2]

            if status == "done":
                list_tasks("done")

            elif status == "todo":
                list_tasks("todo")

            elif status == "in-progress":
                list_tasks("in-progress")

            else:
                print("Invalid status.")

    # UNKNOWN COMMAND
    else:
        print("Unknown command.")


main()