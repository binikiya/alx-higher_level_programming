#!/usr/bin/python3
"""
6-load_from_json_file.py
"""

import json


def load_file_from_json(filename):
    """creates an object from a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
