#!/usr/bin/python3
"""Module that gets information of an employee's TODO list progress
based on the ID given and converts it to CSV format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"

    """Get the JSON dictionaries for users"""
    users = requests.get(user_url).json()
    json_dict = {}

    """Create a list to later add it to a dict to convert to JSON format"""
    for user in users:
        uid = user.get('id')
        task_url = user_url + "/{}/todos".format(uid)
        todos = requests.get(task_url).json()
        username = user.get("username")
        dict_list = []
        for task in todos:
            task_dict = {}
            task_dict["username"] = username
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            dict_list.append(task_dict)
        json_dict[uid] = dict_list

    """Convert list to JSON file"""
    with open("todo_all_employees.json".format(uid), "w") as json_file:
        json_file.write(json.dumps(json_dict))
