#!/usr/bin/python3
"""Module using api to get to do list from employee"""
import requests
"""module that to access command line args""" 
import sys import argv

"""check its the main file and not an import"""
if __name__ == "__main__":
    """retrieve command line arg when running script"""
    uid= argv[1]
    """counter variables to 0 and starts counting from there"""
    all_tasks = 0
    done_task = 0

    """Get JSON doct for requested user and all TODOs"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(uid)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    """retrieves the value associated with the key "name" from dict 'user'
    using the .get() method"""
    name = user.get("name")

    """Get all tasks and completed tasks numbers, and the user completed tasks"""
    """We start with empty list [], if loop then once user id is verified we then add +1 to counter 
    variables until completed task"""
    completed_tasks = []
    for task in todos:
        if int(uid) == task.get('userId'):
            all_tasks += 1
            if task.get('completed') is True:
                done_tasks += 1
                completed_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(name, done_tasks,
                                                          all_tasks))

    """Print all completed tasks' titles"""
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))