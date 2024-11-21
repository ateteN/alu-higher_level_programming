#!/usr/bin/python3
"""
A script that fetches https://alu-intranet.hbtn.io/status using urllib.
It displays the response body, type, content in bytes, and UTF-8 decoded content.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"  # Correct URL

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))

