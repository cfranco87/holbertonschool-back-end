#!/usr/bin/python3
""" USING A REST API THAT RETURN INFORMATION """
import csv
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

    user = name[0].get("username")

    _file = argv[1] + ".csv"

    with open(_file, "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in all_t:
            title = task.get("title")
            complete = task.get("completed")
            id_user = task.get("userId")
            csv_writer.writerow([id_user, user, complete, title])
