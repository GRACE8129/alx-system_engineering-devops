#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after=None):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    """
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
        return
    
    try:
        results = response.json().get("data", {})
        after = results.get("after")
        children = results.get("children", [])
        
        for child in children:
            title = child.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                lower_word = word.lower()
                count = title.count(lower_word)
                if count > 0:
                    if lower_word in instances:
                        instances[lower_word] += count
                    else:
                        instances[lower_word] = count

        if after:
            count_words(subreddit, word_list, instances, after)
        else:
            if instances:
                sorted_words = sorted(instances.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
    except ValueError:
        return