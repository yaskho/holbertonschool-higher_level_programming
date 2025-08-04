#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to the database and delete states containing 'a' in their name."""
    if len(sys.argv) != 4:
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Find all states with 'a' in their name (case-sensitive)
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
