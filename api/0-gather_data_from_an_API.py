#!/usr/bin/python3
""" USING A REST API THAT RETURN INFORMATION """
import requests
from sys import argv

if __name__ == "__main__":
    """ prints info about employee """

    employee = requests.get("http://jsonplaceholder.typicode.com/users?id={}"
                            .format(argv[1]))
    all_tks_user = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    try:
        name = employee.json()
        all_t = all_tks_user.json()

    except ValueError:
        print("Not Valid JSON")

    task_complete = 0
    complete = []

    for task in all_t:
        if task.get("completed") is True:
            task_complete += 1
            complete.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name[0].get("name"), task_complete, len(all_t)))

    for title in complete:
        print("\t {}".format(title))
