#API de recuperation des donnees JSON
#donnees propres
import csv
def fonction_import_donnees_JSON(chemin_fichier):
    #Les besoins :
    """_summary_
    chemin du fichier 
    lire fichier 
    parcourire retourner sous forma de liste ou dictionnaire
    Du module csv/JSON
    """
    try:
        with open(chemin_fichier) as f:
            donnee = csv.DictReader(f)
            apprenant = [(ligne) for ligne in donnee]
        return {"apprenants": apprenant}
    except Exception as e:
        return {"error": str(e)} 


#Definition de l'api qui retourne tout les etudiants dans le fichier JSON
app.get('/api/v1/importationJson')
def get_all_stutends():
    fonction_import_donnees_JSON('donnee_propre.csv')

