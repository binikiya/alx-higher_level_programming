#!/usr/bin/python3
"""
takes your GitHub credentials and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    name, psd = sys.argv[1], sys.argv[2]
    hdr = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/user"
    r = requests.get(url,  auth=(name, psd), headers=hdr)
    print(r.json()["id"])
