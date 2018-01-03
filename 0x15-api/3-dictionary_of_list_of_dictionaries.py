#!/usr/bin/python3


def mass_save_to_json(users):
    """ Output to json format """

    jsondict = {}
    for user in users:
        userid = user.get('id')
        username = user.get('username')
        tasks = user.get('tasks')

        for task in tasks:
            task['task'] = task.pop('title')
            task.pop('id')
            task.pop('userId')
            task['username'] = username

        jsondict[userid] = tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(jsondict, jsonfile)


if __name__ == "__main__":
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url).json()

    users = response

    for user in users:

        url = "https://jsonplaceholder.typicode.com/todos"
        param = {'userId': user.get('id')}
        tasks = requests.get(url, params=param).json()

        user['tasks'] = tasks  # link list of tasks with respective user

    mass_save_to_json(users)
