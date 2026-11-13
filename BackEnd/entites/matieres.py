from pydantic import BaseModel
import psycopg


class Matiere(BaseModel):
    id: int
    nom : str

#definition de la connexion à la base de données
conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()

#Ajouter une matiere
def ajouter_matiere(nommatiere: str):
    try:
            cursor.execute("INSERT INTO matieres (nom) VALUES (%s) RETURNING id", (nommatiere,))
            matiere_result = cursor.fetchone()
            conn.commit()
            return matiere_result
    except Exception as e:
        conn.rollback()
        raise e


#Récupérer toutes les matières
def get_matieres():
    cursor.execute("SELECT * FROM matieres")
    return cursor.fetchall()

#Récupérer une matière par son nom
def get_matiere(nom: str):
    cursor.execute("SELECT * FROM matieres WHERE nom = %s", (nom,))
    return cursor.fetchone()


