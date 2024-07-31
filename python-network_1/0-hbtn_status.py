#!/usr/bin/python3
import urllib.request

# Define the URL
url = "https://alu-intranet.hbtn.io/status"

# Fetch and display the content
with urllib.request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
