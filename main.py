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

if sys.argv[1] == "add":
    print("Adding task: ")
    print(sys.argv[2])

    with open("tasks.json", "r") as f:
        tasks = json.load(f)
        tasks.append(sys.argv[2])
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

elif sys.argv[1] == "update":
    print("Updating task: ")
    print(sys.argv[2])

elif sys.argv[1] == "delete":
    print("Deleting task: ")
    print(sys.argv[2])