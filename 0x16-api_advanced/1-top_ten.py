#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def top_ten(subreddit):
    "prints the titles of the first 10 hot posts listed for a given subreddit"
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
