#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status and prints the response.
"""
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Send GET request
    response = requests.get(url)

    # Display response
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
