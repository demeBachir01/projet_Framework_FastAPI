from pydantic import BaseModel
import psycopg  


class NoteDevoir(BaseModel):
    id: int
    idAppMat : int
    valeur: float

#definition de la connexion à la base de données
conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()

#Ajouter une note
def ajouter_note(idAppMat: int, note: float):
    try:
        cursor.execute("INSERT INTO notesdev (idAppMat, valeur) VALUES (%s, %s)",
                       (idAppMat, note))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e

