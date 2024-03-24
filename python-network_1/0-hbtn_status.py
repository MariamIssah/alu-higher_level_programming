#!/usr/bin/python3
import urllib.request

url = 'http://0.0.0.0:5050/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", utf8_content)
