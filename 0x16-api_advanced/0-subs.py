#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ return number of  subscribers for given subreddit """
    res = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            params={"raw_json": 1},  headers={"User-Agent": "Noop Lion"},  allow_redirects=False)

    return res.json()

