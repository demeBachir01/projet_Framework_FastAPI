
from pydantic import BaseModel
import psycopg

class Classe(BaseModel):
    id: int | None
    nom: str

#Definition de la connexion à la base de données
conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()


#Ajouter une classe
def ajouter_classe(nomClasse: str):
    try:
            # Requetes d'insertion d'une classe
            cursor.execute("INSERT INTO classes (nom) VALUES (%s) RETURNING id", (nomClasse,))
            conn.commit()
            return cursor.fetchone()
    except Exception as e:
        conn.rollback()
        raise e

#Récupérer toutes les classes
def get_classes():
        cursor.execute("SELECT * FROM classes")
        return cursor.fetchall()

#Recuperer classe a partir de son nom
def get_classe(nom: str):
    cursor.execute("SELECT * FROM classes WHERE nom = %s", (nom,))
    return cursor.fetchone()

#Récupérer les apprenants d'une classe
def get_apprenants_classe(id: int):
    cursor.execute("SELECT nom FROM classes WHERE id = %s", (id,))
    return cursor.fetchall()

#Modifier une classe
def modifier_classe(id: int, nomClasse: str):
    try:
        cursor.execute("UPDATE classes SET nom = %s WHERE id = %s", (nomClasse, id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e


