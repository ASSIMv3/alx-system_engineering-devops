#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'task2api'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = response.json()['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
