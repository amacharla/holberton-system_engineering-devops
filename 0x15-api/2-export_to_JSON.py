#!/usr/bin/python3


def save_to_json(user):
    """ Output to json format """

    userid = user.get('id')
    username = user.get('username')
    tasks = user.get('tasks')

    for task in tasks:
        task['task'] = task.pop('title')
        task.pop('id')
        task.pop('userId')
        task['username'] = username

    with open('{}.json'.format(userid), 'w') as jsonfile:
        json.dump({userid: tasks}, jsonfile)

if __name__ == "__main__":
    import requests
    import json
    from sys import argv

    if len(argv) != 2:
        raise Exception("Need to pass in the User id")

    url = "https://jsonplaceholder.typicode.com/users"
    param = {'id': argv[1]}
    response = requests.get(url, params=param).json()

    if len(response) != 1:
        raise Exception("Invalid User Id")

    user = response[0]

    url = "https://jsonplaceholder.typicode.com/todos"
    param = {'userId': user.get('id')}
    tasks = requests.get(url, params=param).json()

    user['tasks'] = tasks  # link list of tasks with respective user

    save_to_json(user)
