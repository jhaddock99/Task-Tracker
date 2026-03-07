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

# Adding a task
if sys.argv[1] == "add":
    print("Adding task: ")
    # Print the task that the user wants to add
    print(sys.argv[2])
    # Define the task that the user wants to add
    task = sys.argv[2]

    # First, we need to check if the json file exists
    try:
        # Try to open the json
        with open("task_list.json", "r") as f:
            task_list = json.load(f)
    
    # If the json file does not exist, catch this with a FileNotFoundError
    except FileNotFoundError:
        task_list = []

    # Write the task to task_list.json
    with open("task_list.json", "w") as f:
        task_list.append(task)
        json.dump(task_list, f)



elif sys.argv[1] == "update":
    print("Updating task: ")
    print(sys.argv[2])


elif sys.argv[1] == "delete":
    print("Deleting task: ")
    print(sys.argv[2])