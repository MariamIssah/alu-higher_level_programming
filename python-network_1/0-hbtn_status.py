#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        utf8_content = html_content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(html_content))
        print("\t- content:", html_content)
        print("\t- utf8 content:", utf8_content)
