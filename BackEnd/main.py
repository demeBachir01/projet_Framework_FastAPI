
import csv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Importation des services
from entites.NoteDevoir import ajouter_note
from entites.apprenant import Apprenants,get_all_apprenants, ajouter_apprenant, get_notes_apprenant, modifier_apprenant, archiver_apprenant, get_apprenants, get_apprenant, get_apprenants_classe,restorer_apprenant
from entites.apprenant_matieres import ajouter_matiere_apprenant,  ajouter_note_examen_apprenant, get_apprenant_matiere
from entites.classes import ajouter_classe, get_classe, modifier_classe
from entites.matieres import ajouter_matiere, get_matiere


#Definition des classes pour les etudiants, les notes, les matieres et les classes


 
#Initialisation de l'application FastAPI
app = FastAPI()

# Configuration CORS indispensable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Les endpoints de l'API pour les apprenants

#Recuperation de tous les apprenants 
@app.get("/api/v1/etudiant")
def get_apprenants():
    try:
        result = get_all_apprenants()
        return result
    except Exception as e:
        return {"error": str(e)}

#Archiver un apprenant
@app.delete("/api/v1/etudiant/{numero}/archiver")
def archive_apprenant(numero: str):
    try:
        archiver_apprenant(numero)
        return {"message": "Apprenant archivé avec succès"}
    except Exception as e:
        return {"error": str(e)}
    
#Restorer un etudiant
@app.patch("/api/v1/etudiant/{numero}/restorer")    
def restore_apprenant(numero:str):
    try :
        restorer_apprenant(numero)
        return {"message": "Apprenant restorer avec succès"}
    except Exception as e :
        return {"error": str(e)}
    
#Ajouter un apprenant
@app.post("/api/v1/etudiant")
def add_apprenant(apprenant: Apprenants):
    try:
        app = ajouter_apprenant(apprenant)
        return app
    except Exception as e:
        return {"error": str(e)}

#Modifier un apprenant
@app.put("/api/v1/etudiant/{numero}")
def update_apprenant(numero: str, apprenant: Apprenants):
    try:
        modifier_apprenant(numero, apprenant)
        return {"message": "Apprenant modifié avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Recuperer un apprenant par son numero
@app.get("/api/v1/etudiant/{numero}")
def get_apprenant_by_numero(numero: str):
    try:
        apprenant = get_apprenant(numero)
        if apprenant:
            return apprenant
        else:
            return {"message": "Apprenant non trouvé"}
    except Exception as e:
        return {"error": str(e)}

#CRUD pour classes

#Ajouter une classe
@app.post("/api/v1/classe/add")
def add_classe(nomClasse: str):
    try:
        clss = ajouter_classe(nomClasse)
        return {"idClasse":clss}
    except Exception as e:
        return {"error": str(e)}

#Recuperer une classe par son nom
@app.get("/api/v1/classe/{nom}")
def get_classe_by_nom(nom: str):
    try:
        classe = get_classe(nom)
        if classe:
            return classe
        else:
            return {"message": "Classe non trouvée"}
    except Exception as e:
        return {"error": str(e)}

#Recuperer les apprenants d'une classe
@app.get("/api/v1/classe/apprenants/{nom}")
def get_apprenants_by_classe(nom: str):
    try:
        apprenants = get_apprenants_classe(nom)
        return {"apprenants": apprenants}
    except Exception as e:
        return {"error": str(e)}
    

#Modifier une classe
@app.put("/api/v1/classe/{nom}")
def update_classe(nom: str, new_nom: str): 
    try:
        classe = get_classe(nom)
        if classe:
            modifier_classe(classe[0], new_nom)
            return {"message": "Classe modifiée avec succès"}
        else:
            return {"message": "Classe non trouvée"}
    except Exception as e:
        return {"error": str(e)}
    

#CRUD pour les matieres

#Ajouter une matiere
@app.post("/api/v1/matiere/add")
def add_matiere(nomMatiere: str):
    try:
        ajouter_matiere(nomMatiere)
        return {"message": "Matière ajoutée avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Recuperer une matiere par son nom
@app.get("/api/v1/matiere/{nom}")
def get_matiere_by_nom(nom: str):
    try:
        matiere = get_matiere(nom)
        if matiere:
            return matiere
        else:
            return {"message": "Matière non trouvée"}
    except Exception as e:
        return {"error": str(e)}

#CRUD pour apprenant-matiere
#Ajouter un apprenant dans une matière
@app.post("/api/v1/etudiant/matiere/")
def ajouter_apprenant_matiere(numero: str, idMatiere: int):
    try:
        ajouter_matiere_apprenant(numero, idMatiere)
        return {"message": "Apprenant ajouté à la matière avec succès"}
    except Exception as e:
        return {"error": str(e)}


#Ajouter une note d'examen pour un apprenant dans une matière
@app.post("/api/v1/etudiant/matiere/noteExamen/")
def ajouter_note_examen(numero: str, idMatiere: int, noteExamen: float):
    try:
        ajouter_note_examen_apprenant(numero, idMatiere, noteExamen)
        return {"message": "Note d'examen ajoutée avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Ajouter une note de devoir pour un apprenant dans une matière
@app.post("/api/v1/etudiant/matiere/noteDevoir/")
def ajouter_note_devoir(numero: str, idMatiere: int, noteDevoir: float):
    try:       
        apprenant_matiere = get_apprenant_matiere(numero, idMatiere)
        if not apprenant_matiere:
            return {"message": "L'apprenant n'est pas inscrit à cette matière"}
        print(apprenant_matiere[1])
        print(apprenant_matiere[2])
        print(apprenant_matiere[0])
        print(apprenant_matiere[3])
        print(noteDevoir)
        ajouter_note(apprenant_matiere[0], noteDevoir)
        return {"message": "Note de devoir ajoutée avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Récupérer les matières d'un apprenant
@app.get("/api/v1/etudiant/matieres/{numero}")
def get_matieres_apprenant(numero: str):
    try:
        matieres = get_matieres_apprenant(numero)
        return {"matieres": matieres}
    except Exception as e:
        return {"error": str(e)}

#Récupérer les notes d'un apprenant
@app.get("/api/v1/etudiant/notes/{numero}")
def get_apprenant_notes(numero: str):
    try:
        notes = get_notes_apprenant(numero)
        return {"notes": notes}
    except Exception as e:
        return {"error": str(e)}


 #Recuperation des donnes dans le fichier JSON
@app.get("/api/v1/importation")
def import_data():
    try:
        with open('donnees_propre.csv') as f:
            donnee = csv.DictReader(f)
            apprenant = [(ligne) for ligne in donnee]
        return {"apprenants": apprenant}
    except Exception as e:
        return {"error": str(e)} 

#Recuperer les apprenants 
