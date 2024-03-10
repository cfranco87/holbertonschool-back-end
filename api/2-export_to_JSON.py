#!/usr/bin/python3
"""comentss"""
from requests import get
from sys import argv
import json

if __name__ == '__main__':
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    ourdata = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    for x in data2:
        if x['id'] == int(argv[1]):
            employee = x['username']
            id_no = x['id']

    ourdata = []

    for x in data:
        new_dict = {}
        if x['userId'] == int(argv[1]):
            new_dict['username'] = employee
            new_dict['task'] = x['title']
            new_dict['completed'] = x['completed']
            ourdata.append(new_dict)

    final_dict = {}
    final_dict[id_no] = ourdata
    json_obj = json.dumps(final_dict)

    with open(argv[1] + '.json', 'w') as file:
        file.write(json_obj)
