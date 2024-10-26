# Calculatrice en Notation Polonaise Inverse (NPI)

Ce projet est une calculatrice en notation polonaise inverse (NPI). Il inclut une API pour calculer les expressions en NPI, enregistrer les opérations dans une base de données, et exporter l'historique des calculs au format CSV. Elle comprend un frontend interactif qui donne des retours visuels en fonction des résultats (succès, erreurs). L’application est conteneurisée avec Docker, ce qui permet un déploiement simple et rapide.

   ### Technologies Utilisées
* Frontend : React, CSS
* Backend : FastAPI, Python
* Base de Données : PostgreSQL (optionnel pour un stockage des calculs)
* Conteneurisation : Docker et Docker Compose


## Table des Matières 
1. [Prérequis]
2. [Fonctionnalités]
3. [Installation et Configuration]
4. [Utilisation]
5. [Tests]
6. [Déploiement]
7. [Contributions]
8. [Ressources et Références]
9. [Auteurs]


---

## 1. Prérequis

- **Docker** et **Docker Compose**
- **Node.js** et **npm** pour le frontend

---

## 2. Fonctionnalités

- Calcul de l’expression en NPI avec validation d’entrée.
-  Affichage d’un message de félicitations si la réponse est correcte, et un message d’erreur sinon.
-  Design inspiré d’une vraie calculatrice avec des éléments visuels amusants (émoticônes de réussite/échec).
-  Intégration d’une API REST avec FastAPI pour gérer les calculs.
-  Conteneurisation avec Docker pour pour simplifier le déploiement.


---

## 3. Installation et Configuration

### Clonez le dépôt et accédez au répertoire :

```bash 
git clone https://github.com/Coralistone/npi_calculator-Test.git
cd npi_calculator
``` 
### Configuration des Variables d’Environnement 
Créez un fichier .env dans le dossier racine pour configurer la base de données (si elle est utilisée).

Exemple de .env :
```bash 
DATABASE_URL=postgresql+asyncpg://postgres:password@db/npi_calculator
```
### Installation du Backend
Dans le dossier app, installez les dépendances Python :
```bash 
cd app
pip install -r requirements.txt
```

### Installation du Frontend
 installez les dépendances npm :
```bash 
npm install 
```
--- 

## 4. Utilisation
### Démarrer le Projet en Local
1. Démarrer le Backend
```bash 
uvicorn main:app --reload
```

2. Démarrer le Frontend 
```bash 
npm start 
```
2. Utiliser la calculatrice 
Rendez-vous sur <http://localhost:3000> pour utiliser la calculatrice.

### Exemple d’Expression NPI
Pour calculer l'expression 12 3 * 4 +, saisissez cette expression dans le champ de saisie, puis appuyez sur le bouton Calculer.

--- 

## 5. Tests
Les tests du backend sont écrits avec pytest.

## 6. Déploiement
Pour déployer l’application avec Docker, suivez ces étapes :

### Build et Démarrage des Conteneurs
Depuis la racine du projet, lancez la commande suivante: 
```bash 
docker-compose up --build 
```
### Accéder à l’Application 
- Frontend : <http://localhost:3000>
- Backend API : <http://localhost:8000/docs> pour la documentation interactive de l’API.

## 7. Contributions
Les contributions sont les bienvenues ! Pour contribuer:
- Forkez le projet.
- Créez une branche pour votre fonctionnalité (git checkout -b feature/NouvelleFonctionnalité).
- Committez vos changements (git commit -m 'Ajout d’une nouvelle fonctionnalité').
- Poussez votre branche (git push origin feature/NouvelleFonctionnalité).
- Ouvrez une Pull Request.
- 
## 8. Ressources et Références
- FastAPI Documentation (<https://fastapi.tiangolo.com/>)
- React Documentation (<https://react.dev/>)
- Docker Documentation (<https://docs.docker.com/>)

## 9. Auteurs
Coralistone METSA - Développeur principal - [Mon git](<https://github.com/Coralistone)>




