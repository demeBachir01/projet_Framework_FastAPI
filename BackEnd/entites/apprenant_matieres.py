from pydantic import BaseModel
import psycopg

from entites.NoteDevoir import NoteDevoir, ajouter_note
from entites.matieres import Matiere

class ApprenantMatiere(BaseModel):
    idAppMat : int
    matiere : Matiere
    noteExam : float | None

#definition de la connexion à la base de données
conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()

#Récupérer les matières d'un apprenant
def get_matieres_apprenant(numero: str):
    cursor.execute("""
        SELECT DISTINCT m.* FROM matieres m
        JOIN apprenant_matiere am ON am.idMatiere = m.id
        WHERE am.numero = %s
    """, (numero,))
    return cursor.fetchall()

#Ajouter une matière à un apprenant
def ajouter_matiere_apprenant(numero: str, idMatiere: int):
    try:
        cursor.execute("INSERT INTO apprenant_matiere (numero, idMatiere) VALUES (%s, %s)",
                       (numero, idMatiere))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
#Ajouter une note d'examen à un apprenant pour une matière donnée
def ajouter_note_examen_apprenant(numero: str, idMatiere: int, note: float):
    try:
        # Ajouter la note d'examen et récupérer son ID
        # Mettre à jour la table apprenant_matiere avec l'ID de la note d'examen
        cursor.execute("UPDATE apprenant_matiere SET noteExam = %s WHERE numero = %s AND idMatiere = %s",
                       (note, numero, idMatiere))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e

#Recupere apprenant-matiere a partir du numero de l'apprenant et de l'id de la matiere
def get_apprenant_matiere(numero: str, idMatiere: int):
    cursor.execute("""
        SELECT am.idAppMat, m.id, m.nom, am.noteExam
        FROM apprenant_matiere am
        JOIN matieres m ON am.idMatiere = m.id
        WHERE am.numero = %s AND am.idMatiere = %s
    """, (numero, idMatiere))
    return cursor.fetchone()
