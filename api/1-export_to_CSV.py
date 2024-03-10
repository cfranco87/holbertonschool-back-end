#!/usr/bin/python3
"""coments"""


from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    ourdata = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    for x in data2:
        if x['id'] == int(argv[1]):
            employee = x['username']

    with open(argv[1] + '.csv', 'w', newline='') as f:
        writ = csv.writer(f, quoting=csv.QUOTE_ALL)

        for x in data:
            ourdata = []
            if x['userId'] == int(argv[1]):
                ourdata.append(x['userId'])
                ourdata.append(employee)
                ourdata.append(x['completed'])
                ourdata.append(x['title'])
                writ.writerow(ourdata)
