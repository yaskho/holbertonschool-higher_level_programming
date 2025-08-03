#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
Results sorted by cities.id ascending.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()

    # Execute query joining cities and states, sorting by cities.id ascending
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all results and print each row
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
