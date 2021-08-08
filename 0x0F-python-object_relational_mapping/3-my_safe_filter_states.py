#!/usr/bin/python3
""" Get state by paremeter but with safe mode """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    find = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    query = """ SELECT states.id, name
    FROM states
    WHERE name = %s
    ORDER BY states.id ASC;
    """
    
    cur.execute(query, (find, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()