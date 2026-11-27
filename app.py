
# Import required libraries
from flask import Flask, render_template, request, redirect
from pathlib import Path
from uuid import uuid4
import json

# Initialize Flask application
app = Flask(__name__)

# Define project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"
CONFIG_FILE = BASE_DIR / "config" / "settings.json"


# Load existing tasks
def load_tasks():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    return []


# Save tasks into the JSON file
def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# Display the main page
@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


# Add a new task
@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task", "").strip()

    if task_name:
        tasks = load_tasks()

        new_task = {
            "id": str(uuid4()),
            "name": task_name,
            "completed": False
        }

        tasks.append(new_task)
        save_tasks(tasks)

    return redirect("/")


# Mark a task as completed
@app.route("/complete/<task_id>", methods=["POST"])
def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break

    save_tasks(tasks)
    return redirect("/")


# Delete a task
@app.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    save_tasks(tasks)
    return redirect("/")


# Start the application
if __name__ == "__main__":
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = json.load(file)

    app.run(
        host=config["host"],
        port=config["port"],
        debug=False
    )
