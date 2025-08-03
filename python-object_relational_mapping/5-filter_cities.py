#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()

    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
