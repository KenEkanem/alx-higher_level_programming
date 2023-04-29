#!/usr/bin/python3
"""Take a URL, send request and display X-Request-Id"""
from urllib.request import urlopen
import sys

def get_request_id(url):
    """Open URL and display X-Request-Id"""
    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <url>')
        sys.exit(1)
    url = sys.argv[1]
    get_request_id(url)

