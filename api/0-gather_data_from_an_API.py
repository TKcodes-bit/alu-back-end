#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID."""

import requests
import sys


def main():
    """Main function to fetch and display TODO progress."""
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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
    response_user = requests.get(url_user)
    user = response_user.json()
    employee_name = user.get("name")

    url_todos = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, done_count, total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
