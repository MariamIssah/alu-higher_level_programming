#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(<class'bytes'>)))
        print("\t- content: {}".format(b'Custom status'))
        print("\t- utf8 content: {}".format("Custom status")))
