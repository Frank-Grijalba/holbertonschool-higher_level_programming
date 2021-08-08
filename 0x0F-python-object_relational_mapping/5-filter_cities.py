#!/usr/bin/python3
""" Show all the cities in the database"""

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
    
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    
    cur.execute(query, (find, ))
    rows = cur.fetchall()
    rows = [i[0] for i in rows]
    print(', '.join(rows))

    cur.close()
    db.close()
    