#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
of the response
"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
