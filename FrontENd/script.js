//Declaration de l'url de l'API
let apiUrl = ' http://127.0.0.1:8000/api/v1/';

let etudiants = [];
let pageActuelle = 1;
let etudiantsParPage = 5;


// etu = etudiants[index];
    //On recupere les notes de chaque matiere
   // note = parseNotes(etu.notes)
    //non_classe = etu.classe


//Fonction d'ajout d'etudiant
async function ajoutEtudiant(etudiant){
   try {
        const response = await fetch(apiUrl + 'etudiant', {
            method : POST,
            headers: {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({etudiant:etudiant})
        });
        if (response.ok) {
            console.log("Classe Ajouter avec succes")
        }
    }
    catch(error) {
        console.log(error)
    }
}

//Fonction ajout classe
async function ajoutClasse(nonClasse){
    try {
        const response = await fetch(apiUrl + 'classe', {
            method : POST,
            headers: {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({ nomClasse: nonClasse })
        });
        if (response.ok) {
            return response.idClasse
            console.log("Classe Ajouter avec succes")
        }
    }
    catch(error) {

    }
}

//Fonction d'ajout d'une classe
async function ajouterMatiere(nomMatiere) {
    try {
        const reponse = await fetch(apiUrl + 'matiere/add',{
            method : POST,
            headers : {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({ matiere: nomMatiere })
        });
        if (response.ok) {
            return response.idClasse
            console.log("Classe Ajouter avec succes")
        }
    }
    catch(error) {
        console.log(error)
    }    
}

//Recuperer classe
async function get_classe(nom) {
    const response = await fetch(apiUrl + 'matiere/${nom}')
    if (!response.ok){
        return null
    }

    const data = await response.json()
    console.log('classe trouver',data)
    return data
}

//Recuperer metiere
async function get_metiere(nomMatiere) {
    const response = await fetch(apiUrl + 'matiere/${nomMatiere}')
    if (!response.ok){
        return null
    }

    const data = await response.json()
    console.log('Matiere trouver',data)
    return data
}


//Recuperation des etudiants du fichier JSON
async function fetchEtudiants() {
    try {
        const response = await fetch(apiUrl + 'importation');
        const data = await response.json();
        //Affichage des etudiants dans la console
        console.log(data);
            etudiants = Array.isArray(data) ? data : data?.apprenants || data?.data || [];
            let note = etudiants[0].notes;
            note = parseNotes(note);
            console.log(note);
            afficherEtudiants(etudiants);
    } catch (error) {
        console.error('Erreur lors de la récupération des étudiants:', error);
    }
}

//Recuperation des etudiants dans la base de donnees
async function donneeBase() {
    try {
        const reponse = await fetch(apiUrl+'/etudiant')
        const data = await reponse.json();

    } catch (error) {
        
    }
}

//Ajouter un etudiant a une matiere
async function ajout_etudiant_matiere(numero, idMatiere) {
    try {
        const response = await fetch(apiUrl + 'etudiant/matiere/?numero=${numero}&idMatiere=${idMatiere}')
        if(response.ok){
            data =  await response.json()
            return data
        }
    } catch (error) {
        console.log(error)
    }    
}


//Fonction pour afficher les etudiants dans le tableau HTML avec pagination
function afficherEtudiants(etudiants, page = 1) {
    pageActuelle = page;
    const tableBody = document.getElementById('etudiantsTableBody');
    tableBody.innerHTML = ''; // Clear previous rows
    
    // Calculer les indices de début et fin
    const debut = (page - 1) * etudiantsParPage;
    const fin = debut + etudiantsParPage;
    
    // Obtenir les étudiants pour cette page
    const etudiantsPage = etudiants.slice(debut, fin);
    
    // Afficher les étudiants
    etudiantsPage.forEach((etudiant, indexPage) => {
        const indexGlobal = debut + indexPage;
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${etudiant.numero}</td>
            <td>${etudiant.nom}</td>
            <td>${etudiant.prenom}</td>
            <td>${etudiant.date_naissance}</td>
            <td>${etudiant.classe}</td>
            <td><button onclick='afficherNotes(${indexGlobal})'>Afficher Notes</button></td>
            <td><button onclick='afficherNotes(${indexGlobal})'>Enregistrer</button></td>
            <td><button onclick='afficherNotes(${indexGlobal})'>Supprimer</button></td>
        `;
        tableBody.appendChild(row);
    });
    
    // Mettre à jour l'affichage de la page
    const totalPages = Math.ceil(etudiants.length / etudiantsParPage);
    document.getElementById('pageInfo').textContent = `Page ${page} / ${totalPages}`;
    
    // Désactiver les boutons si nécessaire
    const buttons = document.querySelectorAll('#paginationControls button');
    buttons[0].disabled = page === 1;
    buttons[1].disabled = page === totalPages;
}

//Fonction de parsing des notes
function parseNotes(notes) {
    try {
        // Remplace les guillemets simples par des guillemets doubles
        const formatNotes = notes.replace(/'/g, '"');
        // Parse la chaîne JSON
        return JSON.parse(formatNotes);
    } catch (error) {
        console.error('Erreur lors du parsing des notes:', error);
        return null;
    }
}

//Fonction pour afficher les notes d'un etudiant
function afficherNotes(index) {
    const notes = parseNotes(etudiants[index].notes);
    const tableNote = document.getElementById('notesContainer')
    tableNote.innerHTML = `<h2>Notes de l'étudiant ${etudiants[index].prenom} ${etudiants[index].nom}</h2>
        <table>
            <thead>
                <tr>
                    <th>Matière</th>
                    <th>Note devoir</th>
                    <th>Note examen</th>
                    <th>Moyenne</th>
                </tr>
            </thead>
            <tbody id="notesTableBody">
            </tbody>
        </table>`
    const tbodyNotes = document.getElementById('notesTableBody'); 
    tbodyNotes.innerHTML = ''; // Clear previous notes
    
    if (!notes) {
        tbodyNotes.innerHTML = '<tr><td colspan="4">Erreur lors du chargement des notes</td></tr>';
        return;
    }
    
    for (const [matiere, donnees] of Object.entries(notes)) {
        const row = document.createElement('tr');
        
        // Calculer la moyenne des devoirs
        let moyenneDevoirs = 0;
        if (Array.isArray(donnees.devoirs) && donnees.devoirs.length > 0) {
            const sommeDevoirs = donnees.devoirs.reduce((sum, note) => sum + note, 0);
            moyenneDevoirs = (sommeDevoirs / donnees.devoirs.length).toFixed(2);
        }
        
        row.innerHTML = `
            <td>${matiere}</td>
            <td>${moyenneDevoirs}</td>
            <td>${donnees.examen}</td>
            <td>${donnees.moyenne.toFixed(2)}</td>
        `;
        tbodyNotes.appendChild(row);
    }

}

//Fonction pour aller à la page suivante
function pageSuivante() {
    const totalPages = Math.ceil(etudiants.length / etudiantsParPage);
    if (pageActuelle < totalPages) {
        afficherEtudiants(etudiants, pageActuelle + 1);
    }
}

//Fonction pour aller à la page précédente
function pagePrecedente() {
    if (pageActuelle > 1) {
        afficherEtudiants(etudiants, pageActuelle - 1);
    }
}

//Fonction pour changer le nombre d'étudiants par page
function changerNombreParPage(nombre) {
    etudiantsParPage = parseInt(nombre);
    pageActuelle = 1; // Réinitialiser à la première page
    afficherEtudiants(etudiants, 1);
}

window.onload = fetchEtudiants;

//Recuperation des etudiants de la base de données
