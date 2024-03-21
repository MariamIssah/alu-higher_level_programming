#!/usr/bin/python3
"""__summary__
- Write a Python script that
- fetches https://intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, headers=headers)

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

