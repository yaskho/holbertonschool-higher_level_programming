#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()

    # SQL query to get cities of the state with given name
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all city names
    cities = cursor.fetchall()

    # Print city names comma separated (no output if no cities found)
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
