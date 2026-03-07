# The goal of this project is to build a task tracker that manages my tasks.
# In this project, I'll build a simple CLI to track what I need to do, what I have done, and what I am currently working on.

# Project requirements:
#   User should be able to:
#    - Add, update, and delete tasks
#    - Mark a task as in progress or done
#    - List all tasks
#    - List all tasks that are done
#    - List all tasks that are not done
#    - List all tasks that are in progress

import sys
import json
from datetime import datetime

# Adding a new task
if sys.argv[1] == "add":
    print("Adding task: " + sys.argv[2])

    try:
        with open("task_list.json", "r") as f:
            task_list = json.load(f)
    
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []

    id = len(task_list) + 1
    task = {
        "id": id,
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    
    with open("task_list.json", "w") as f:
        task_list.append(task)
        json.dump(task_list, f, indent = 4)

# Listing all tasks
elif sys.argv[1] == "list":
    try:
        with open("task_list.json", "r") as f:
            task_list = json.load(f)
    
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []
        print("Task list is empty.")

    for task in task_list:
        task_id = task["id"]
        task_description = task["description"]
        task_status = task["status"]
        print("Task ", task_id, "Description: ", task_description, "Status: " ,task_status)