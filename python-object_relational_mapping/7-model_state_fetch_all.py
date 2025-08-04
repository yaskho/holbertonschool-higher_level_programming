#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupérer les arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Créer le moteur de connexion à MySQL
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}')

    # Créer une session liée à ce moteur
    Session = sessionmaker(bind=engine)
    session = Session()

    # Faire la requête pour récupérer tous les states triés par id
    states = session.query(State).order_by(State.id).all()

    # Afficher le résultat au format demandé
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermer la session
    session.close()
