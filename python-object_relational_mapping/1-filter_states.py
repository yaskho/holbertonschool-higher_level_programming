#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Récupération des arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)

    # Création du curseur
    cursor = db.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
