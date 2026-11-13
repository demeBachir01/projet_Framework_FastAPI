# 🎓 Application de gestion des étudiants

Application web de gestion des étudiants développée avec **FastAPI** pour le backend et **HTML, CSS et JavaScript** pour l'interface utilisateur.

Ce projet met en pratique le développement d'une API REST avec FastAPI et son intégration avec une interface web frontend.

## 🛠️ Technologies utilisées

### Backend
- **Python** : langage de programmation.
- **FastAPI** : framework de développement d'API REST.

### Frontend
- **HTML5** : structure des pages.
- **CSS3** : mise en forme et présentation.
- **JavaScript** : interactions et communication avec le backend.

## 📁 Structure du projet

```text
projet_Framework_FastAPI/
│
├── BackEnd/
│   └── ...
│
├── FrontENd/
│   └── ...
│
├── .gitignore
└── README.md
```

## ⚙️ Installation et exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/demeBachir01/projet_Framework_FastAPI.git
```

### 2. Accéder au projet

```bash
cd projet_Framework_FastAPI
```

### 3. Configurer le backend

Accéder au dossier backend :

```bash
cd BackEnd
```

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement virtuel :

**Windows :**
```bash
venv\Scripts\activate
```

**Linux / macOS :**
```bash
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer le serveur FastAPI (adapter le module et l'objet ASGI au point d'entrée réel du projet) :

```bash
uvicorn main:app --reload
```

### 4. Accéder à l'application

Une fois le serveur démarré :

- API : `http://127.0.0.1:8000`
- Documentation Swagger : `http://127.0.0.1:8000/docs`
- Documentation ReDoc : `http://127.0.0.1:8000/redoc`

Le frontend se lance selon son organisation et son point d'entrée.

## 🎯 Objectifs du projet

- Découvrir et pratiquer le framework FastAPI.
- Concevoir une API REST avec Python.
- Mettre en place une communication entre frontend et backend.
- Développer une interface web avec HTML, CSS et JavaScript.
- Comprendre l'organisation d'une application web séparant frontend et backend.

## 👨‍💻 Auteur

**Bachir DEME**

- GitHub : [@demeBachir01](https://github.com/demeBachir01)
- LinkedIn : [Bachir DEME](https://www.linkedin.com/in/bachir-deme-47a2121a5/)

---

<div align="center">

**Projet réalisé dans le cadre de l'apprentissage du développement backend avec FastAPI.**

</div>