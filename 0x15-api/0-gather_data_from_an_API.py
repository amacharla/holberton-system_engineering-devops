#!/usr/bin/python3
# prints info about employee and there done tasks

def print_for_0(user):
    """ Special output for assignment 0 """

    name = user.get('name')
    tasks = user.get('tasks')
    done = [task.get('title') for task in tasks if
            task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(name, len(done),
                                                          len(tasks)))

    for title in done:
        print('\t{}'.format(title))


if __name__ == "__main__":
    import requests
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

    print_for_0(user)
