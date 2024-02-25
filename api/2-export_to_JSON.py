#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    employee_id = argv[1]
    task_list = []

    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    for task in employee_todos.json():
        task_dict = {"task": task["title"], "completed": task["completed"],
                     "username": employee.json()["username"]}
        task_list.append(task_dict)

    employee_task_dict = {f"{employee_id}": task_list}

    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as file:
        json.dump(employee_task_dict, file)
