
from datetime import date, datetime
import psycopg
from pydantic import BaseModel
from pydantic import BaseModel, field_validator
from psycopg import  cursor

#Importation des autres entités
from entites.NoteDevoir import ajouter_note, NoteDevoir
from entites.classes import Classe, ajouter_classe, get_classe, get_apprenants_classe

# Modèle de données pour un apprenant
class Apprenants(BaseModel):
    code : str
    numero : str
    nom: str
    prenom: str
    date_naissance: date
    idClasse: int
    archived: bool = False

    @field_validator("date_naissance", mode="before")
    @classmethod
    def parser_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y").date()
        return value

# Connexion à la base de données
conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()

#defintion des methodes pour les opérations CRUD sur les apprenants
#Ajouter un apprenant
def ajouter_apprenant(apprenant: Apprenants):
    try:      
        cursor.execute("INSERT INTO apprenants (idClasse, code, numero, nom, prenom, date_naissance, archived) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (apprenant.idClasse, apprenant.code, apprenant.numero, apprenant.nom, apprenant.prenom, apprenant.date_naissance, apprenant.archived))
        conn.commit()
        return cursor.fetchone()
    except Exception as e:
        conn.rollback()
        raise e
  
 
#Modifier les informations d'un apprenant
def modifier_apprenant(numero: str, apprenant: Apprenants):
    try:
        cursor.execute("UPDATE apprenants SET code = %s, nom = %s, prenom = %s, date_naissance = %s, archived = %s WHERE numero = %s",
                       (apprenant.code, apprenant.nom, apprenant.prenom, apprenant.date_naissance, apprenant.archived, numero))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e   

#Archiver un apprenant
def archiver_apprenant(numero: str):
    try:
        cursor.execute("UPDATE apprenants SET archived = TRUE WHERE numero = %s", (numero,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

#Restorer un etudiant
def restorer_apprenant(numero:str):
    try :
        cursor.execute("UPDATE apprenants SET archived = FALSE WHERE numero = %s", (numero,))
        conn.commit()
    except Exception as e :
        conn.rollback()
        raise e        

#Récupérer tous les apprenants non archiver
def get_apprenants():
    cursor.execute("SELECT * FROM apprenants WHERE archived = FALSE")
    return cursor.fetchall()

#Récupérer tous les apprenants  archiver
def get_apprenant_archived():
    cursor.execute("SELECT * FROM apprenants WHERE archived = TRUE")
    return cursor.fetchall()

#Récupérer un apprenant par son numero
def get_apprenant(numero: str):
    cursor.execute("SELECT * FROM apprenants WHERE numero = %s", (numero,))
    return cursor.fetchone()


#Récupérer les apprenants d'une classe
def get_apprenants_classe(nomClasse: str):
    classe = get_classe(nomClasse)
    if not classe:
        return []
    cursor.execute("SELECT * FROM apprenants WHERE idClasse = %s", (classe[0],))
    return cursor.fetchall()

#Récupérer les apprenants non archivés 
def get_all_apprenants():
    try:
        # Pagination des apprenants par 5 par défaut
        cursor.execute("SELECT * FROM apprenants where archived = FALSE")
        apprenants = cursor.fetchall()
       
        return {
            "apprenants": apprenants,
        }
    except Exception as e:
        return {"error": str(e)}

#Récupérer les notes d'un apprenant (via apprenant_matiere)
def get_notes_apprenant(numero: str):
    cursor.execute("""
        SELECT n.valeur, m.nom FROM notesdev n
        JOIN apprenant_matiere am ON n.idAppMat = am.idAppMat
        JOIN matieres m ON am.idMatiere = m.id
        WHERE am.numero = %s
    """, (numero,))
    return cursor.fetchall() 



