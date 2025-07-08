#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url_user = (
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id
        )
    )
    user = requests.get(url_user).json()
    username = user.get("username")

    url_todos = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    todos = requests.get(url_todos).json()

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    data = {str(employee_id): tasks}
    filename = "{}.json".format(employee_id)

    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile)
