#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    # Base URL for JSONPlaceholder
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print the summary
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

