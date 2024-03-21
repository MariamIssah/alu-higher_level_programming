#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status and prints the response.
"""
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"

    # Create a session object
    with requests.Session() as session:
        # Set User-Agent header
        session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        )

        # Send GET request
        r = session.get(url)

        # Display response
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
