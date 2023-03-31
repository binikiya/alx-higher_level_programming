#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    text = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(text), text))
