#!/usr/bin/python3
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print("\t- type:", <class 'bytes'>))
print("\t- content:", b'Custom status')
print("\t- utf8 content:", Custom status)
