#!/usr/bin/python3
"""coments"""


from requests import get
import json

if __name__ == '__main__':
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    ourdata = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    new_dict1 = {}

    for x in data2:
        ourdata = []
        for i in data:
            new_dict2 = {}
            if x['id'] == i['userId']:
                new_dict2['username'] = x['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                ourdata.append(new_dict2)
        new_dict1[x['id']] = ourdata

    with open("todo_all_employees.json", 'w') as file:
        json_obj = json.dumps(new_dict1)
        file.write(json_obj)
