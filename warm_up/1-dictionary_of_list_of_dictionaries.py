#!/usr/bin/python3
"""
Gets all users and there respective todos and combines and output them to JSON
"""

if __name__ == "__main__":
    import requests
    import json

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    results = {}
    for user in users:
        user.update({'tasks': [
            {'username': user['username'],
             'task':task['title'],
             'completed':task['completed']}
            for task in todos if task.get('userId') == user.get('id')]})

        user.pop('address')
        user.pop('company')
        user.pop('email')
        user.pop('name')
        user.pop('phone')
        user.pop('website')
        user.pop('username')

        results.update({user.get('id'): user.get('tasks')})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(results, f)
