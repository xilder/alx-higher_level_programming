#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    with urllib.request.urlopen(req, data) as response:
        body = response.read()
        print(body.decode("utf-8"))
