#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    try:
        results = response.json().get("data", {})
        after = results.get("after")
        children = results.get("children", [])
        
        if not children:
            return None
        
        for child in children:
            hot_list.append(child.get("data", {}).get("title"))
        
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except ValueError:
        return None