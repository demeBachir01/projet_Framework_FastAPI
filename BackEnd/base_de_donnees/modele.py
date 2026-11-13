
   
import psycopg


conn = psycopg.connect("dbname=gestion_ecole user=odc password=passer host=localhost port=5432")
cursor = conn.cursor()

# cursor.execute("""drop table if exists notesdev cascade""")
# cursor.execute("""drop table if exists matieres cascade""")
# cursor.execute("""drop table if exists classes cascade""")
# cursor.execute("""drop table if exists apprenants cascade""")
# cursor.execute("""drop table if exists apprenant_matiere cascade""")

#Création des tables dans la base de données

#Table matieres
cursor.execute("""CREATE TABLE IF NOT EXISTS matieres (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL UNIQUE
)""")

#Table classes
cursor.execute("""CREATE TABLE IF NOT EXISTS classes (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL UNIQUE
)""")

#Table apprenants
cursor.execute("""CREATE TABLE IF NOT EXISTS apprenants (
    idClasse INTEGER REFERENCES classes(id),
    code VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NOT NULL UNIQUE PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    moyenne_generale FLOAT,
    archived BOOLEAN DEFAULT FALSE
)""")

#Table apprenant_matiere
cursor.execute("""CREATE TABLE IF NOT EXISTS apprenant_matiere (
    idAppMat SERIAL PRIMARY KEY,
    numero VARCHAR(10) REFERENCES apprenants(numero),
    idMatiere INTEGER REFERENCES matieres(id),
    noteExam FLOAT,
    moyenne_matiere FLOAT
)""")

#Table notes
cursor.execute("""CREATE TABLE IF NOT EXISTS notesdev (
    id SERIAL PRIMARY KEY,
    idAppMat INTEGER REFERENCES apprenant_matiere(idAppMat),
    valeur FLOAT NOT NULL
)""")

conn.commit()
