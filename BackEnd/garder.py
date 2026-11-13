
#Definition des routes pour les endpoints de l'API
@app.get("/apprenants")

#Ajouter un apprenant
@app.post("/apprenant/add")
def create_apprenant(apprenant: Apprenants):
    try:
        ajouter_apprenant(apprenant)
        return {"message": "Apprenant ajouté avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Modifier un apprenant
@app.put("/apprenant/{numero}")
def update_apprenant(numero: str, apprenant: Apprenants):
    try:
        modifier_apprenant(numero, apprenant)
        return {"message": "Apprenant modifié avec succès"}
    except Exception as e:
        return {"error": str(e)}

#Archiver un apprenant
@app.delete("/apprenant/{numero}")
def delete_apprenant(numero: str):
    try:
        archiver_apprenant(numero)
        return {"message": "Apprenant archivé avec succès"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/notesdev")
def get_all_notesdev():
    try:
        notesdev = get_notesdev()
        return {"notesdev": notesdev}
    except Exception as e:
        return {"error": str(e)}

@app.get("/matieres")
def get_all_matieres():
    try:
        matieres = get_matieres()
        return {"matieres": matieres}
    except Exception as e:
        return {"error": str(e)}

@app.get("/classes")
def get_all_classes():
    try:
        classes = get_classes()
        return {"classes": classes}
    except Exception as e:
        return {"error": str(e)}

@app.get("/apprenants/{numero}/notes")
def get_apprenant_notes(numero: str):
    try:
        notes = get_notes_apprenant(numero)
        return {"notes": notes}
    except Exception as e:
        return {"error": str(e)}

@app.get("/apprenants/{numero}/matieres")
def get_apprenant_matieres(numero: str):
    try:
        matieres = get_matieres_apprenant(numero)
        return {"matieres": matieres}
    except Exception as e:
        return {"error": str(e)}

@app.get("/apprenants/{numero}/classes")
def get_apprenant_classes(numero: str):
    try:
        classes = get_classes_apprenant(numero)
        return {"classes": classes}
    except Exception as e:
        return {"error": str(e)}

@app.get("/classe/{idClasse}")
def get_class_apprenants(idClasse: int):
    try:
        nomClasse = get_apprenants_classe(idClasse)
        return {"nomClasse": nomClasse}
    except Exception as e:
        return {"error": str(e)}

#Chargenment des donnees valide du fichier csv
with open('donnees_propre.csv') as f:
    donnee = csv.DictReader(f)
    apprenant = [(ligne) for ligne in donnee]

@app.get("/test")
def test():
    #Traitement de la note des devoirs et des examens pour chaque apprenant
    for appr in apprenant:
        pass
    return {"apprenants": apprenant}