#!/usr/bin/python3


def print_to_csv(user):
    """ Output to CSC format """

    userid = user.get('id')
    username = user.get('username')
    tasks = user.get('tasks')

    with open('{}.csv'.format(userid), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow((userid, username, task.get('completed'),
                             task.get('title')))


if __name__ == "__main__":
    import requests
    import csv
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

    print_to_csv(user)
