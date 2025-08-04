#!/usr/bin/python3
"""
Prints the first State object from the database.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id.asc()).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

if __name__ == "__main__":
    main()
