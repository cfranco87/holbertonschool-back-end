#!/usr/bin/python3
"""
   export the data to Json.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    """
        api function
    """

    api_url = f'https://jsonplaceholder.typicode.com/'

    user_id = (argv[1])
    user_data = requests.get(api_url + f'users/{user_id}').json()
    task_todo = requests.get(api_url + f'users/{user_id}/todos').json()

    task_dict = []
    for task in task_todo:
        completed_tasks = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_data["username"]
            }
        task_dict.append(completed_tasks)

        with open(f'{user_id}.json', 'w') as file:
            json.dump({user_id: task_dict}, file)
