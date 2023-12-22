#!/usr/bin/python3
"""Module that gets information of an employee's TODO list progress
based on the ID given and converts it to CSV format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    task_url = user_url + "/todos"

    """Get the JSON dictionaries for requested user and all TODOs"""
    user = requests.get(user_url).json()
    todos = requests.get(task_url).json()

    username = user.get("username")

    """Create a list to later convert to JSON format"""
    dict_list = []
    for task in todos:
        row = {}
        row["task"] = task.get("title")
        row["completed"] = task.get("completed")
        row["username"] = username
        dict_list.append(row)
    json_dict = {}
    json_dict[uid] = dict_list

    """Convert list to JSON file"""
    with open("{}.json".format(uid), "w") as json_file:
        json_file.write(json.dumps(json_dict))