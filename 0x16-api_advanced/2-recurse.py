#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[]):
    """ returns a list containing the titles of all hot articles for a given
    subreddit.
    If no results are found for the given subreddit,
    the function should return None. """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            recurse(subreddit, hot_list, next_)
        titles_list = response.json().get('data').get('children')
        for title in titles_list:
            hot_list.append(title.get('data').get('title'))
        return (hot_list)
    return (None)
