#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """print the titles"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'user-agent': 'API-Client'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
