#!/usr/bin/python3
"""Module using api to get to do list from employee"""
"""module that to access command line args"""

import requests
import sys
from sys import argv



"""check its the main file and not an import"""
if __name__ == "__main__":
    """retrieve command line arg when running script"""
    uid = argv[1]

    """counter variables to 0 and starts counting from there"""
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    """Get JSON doct for requested user and all TODOs"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(uid)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    """retrieves the value associated with the key "name" from dict 'user'
    using the .get() method"""
    EMPLOYEE_NAME = user.get("name")

    """Get all tasks and completed tasks numbers, and the user completed task.
    We start with empty list [], if loop then once user id is verified we then
    add +1 to counter variables until completed task"""
    completed_tasks = []
    for task in todos:
        if int(uid) == task.get('userId'):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                completed_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS
    ))

    """Print all completed tasks titles"""
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
