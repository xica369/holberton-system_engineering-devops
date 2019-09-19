#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0."""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
