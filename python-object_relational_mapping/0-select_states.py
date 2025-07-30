#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Récupérer les arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Exécuter la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer tous les résultats
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
