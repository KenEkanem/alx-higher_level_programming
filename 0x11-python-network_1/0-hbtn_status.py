#!/usr/bin/python3
"""fetch url with urlib"""
from urllib.request import urlopen

def fetch_status():
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        print('Fetching status...')
        print(f'Status code: {response.status}')
        print(f'Content type: {response.headers["Content-Type"]}')
        print('Body:')
        print(decoded_body)


if __name__ == '__main__':
    fetch_status()

