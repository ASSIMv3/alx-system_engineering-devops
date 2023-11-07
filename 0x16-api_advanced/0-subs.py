#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subs"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subs"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-agent': 'API-Client'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        return subscribers
    else:
        return 0
