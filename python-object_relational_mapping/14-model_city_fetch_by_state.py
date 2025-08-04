#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa,
sorted by cities.id ascending, with their State name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    if len(sys.argv) != 4:
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities sorted by id ascending
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        # Get the state linked to this city (foreign key state_id)
        state = session.query(State).filter(State.id == city.state_id).first()
        if state:
            print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()
