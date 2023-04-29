#!/usr/bin/python3
"""Send POST request to URL with email parameter"""
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import sys


def send_post_request(url, email):
    """Send POST request with email parameter and display response body"""
    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 script.py <url> <email>')
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)

