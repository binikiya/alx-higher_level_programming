#!/usr/bin/python3
"""
takes in argument and displays all values in the states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()
