#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID."""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url_user = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    response_user = requests.get(url_user)
    user = response_user.json()
    employee_name = user.get("name")

    url_todos = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
