#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument,
safe from MySQL injections.
Usage: ./3-my_safe_filter_states.py <mysql_user> <mysql_password> <db_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
