#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests
after = None
count_dic = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords """
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            count_words(subreddit, word_list)
        list_objs = response.json().get('data').get('children')
        for obj in list_objs:
            for word in word_list:
                title_list = (title_.get('data').get('title')).split()
                if word in title_list:
                    count_dic[word] = count_dict.keys() + 1
        sort_dic = sorted(count_dic.items(), key=operator.itemgetter(1))
        sort_dic = sort_dic.reverse()
        for key, value in sort_dic.items():
            print("{}: {}".format(key, value))
    else:
        print()
