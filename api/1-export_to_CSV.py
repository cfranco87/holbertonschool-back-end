#!/usr/bin/python3
import csv
import requests
from sys import argv
"""Module using api to get to do list from employee"""
"""module that to access command line args"""
"""CSV format for storing tubalar data(number and text)"""


"""check its the main file and not an import"""
if __name__ == "__main__":
    """retrieve command line arg when running script"""
    uid = argv[1]
    """fetches the user data in JSON format from the specified URL"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    task_url = user_url + "/todos"

    """Get the JSON dict for requested user and todos"""
    user = requests.get(user_url).json()
    todos = requests.get(task_url).json()

    """variables for each string represents a column header in the CSV file"""
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    username = user.get("username")

    """Create a list to later convert to csv format"""
    csv_list = []
    for task in todos:
        """empty dict for row on table"""
        row = {}
        """ organizes the data retrieved from the user's TODO list 
        into a structure suitable for CSV export"""
        row["USER_ID"] = task.get("userId")
        row["USERNAME"] = username
        row["TASK_COMPLETED_STATUS"] = task.get("completed")
        row["TASK_TITLE"] = task.get("title")
        """adds dict to list"""
        csv_list.append(row)

    """codeblock responsible with opening CSV file"""
    with open("{}.csv".format(uid), "w") as csv_file:
        """It is specifically designed for writing dictionaries to CSV files."""
        csv_ins = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                 quoting=csv.QUOTE_ALL)
        """line writes multiple rows to the CSV file"""
        csv_ins.writerows(csv_list)