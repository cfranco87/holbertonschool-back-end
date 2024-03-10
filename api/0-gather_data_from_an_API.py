#!/usr/bin/python3
"""function to gather the data from API"""

import requests
from sys import argv


if __name__ == '__main__':

    api_url = f'https://jsonplaceholder.typicode.com/'

    user_id = (argv[1])
    user_data = requests.get(api_url + f'users/{user_id}').json()
    task_todo = requests.get(api_url + f'users/{user_id}/todos').json()
    completed_task = [task for task in task_todo if task['completed']]

    print(f'Employee {user_data["name"]} is done with', end='')
    print(f' task({len(completed_task)}/{len(task_todo)}):')

    for tasks in completed_task:
        print("\t" + tasks["title"])
