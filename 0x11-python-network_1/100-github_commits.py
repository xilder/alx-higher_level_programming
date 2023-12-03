#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    response = requests.get(url).json()
    try:
        for i in range(10):
            sha = response[i].get("sha")
            owner = response[i].get("commit").get("author").get("name")
            print(f"{sha}: {owner}")
    except IndexError:
        pass
