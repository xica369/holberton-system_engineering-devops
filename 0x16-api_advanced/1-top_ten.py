#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def top_ten(subreddit):
    "prints the titles of the first 10 hot posts listed for a given subreddit"
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
    print(None)
