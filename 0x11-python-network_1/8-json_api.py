#!/usr/bin/python3
"""
a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        datum = {"q": argv[1]}
    else:
        datum = {"q": ""}

    try:
        response = requests.post(url, data=datum).json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError as json_err:
        print("Not a valid JSON")
