#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    conn.close()
