#!/usr/bin/python3
"""__summary__
- Write a Python script that
- fetches https://intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url, allow_redirects=True)

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
