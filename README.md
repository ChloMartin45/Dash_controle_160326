# Projet Avocado – Analyse et Visualisation du Marché des Avocats

Avocado est une application interactive développée avec Dash, permettant d'explorer, de visualiser et de comparer les données de vente d'avocats aux États-Unis. Elle offre des outils d'analyse tabulaire et graphique pour comprendre l'évolution des prix et des volumes selon les régions et les types de produits.

---

## 🌟 Fonctionnalités principales

### 1. **Exploration des données (Tableau)**
- Filtrage dynamique par région et par type (Conventionnel ou Biologique).
- Gestion intelligente de l'option "Tous" pour une vue globale.
- Nettoyage automatique des colonnes techniques (IDs, volumes spécifiques) pour une lecture simplifiée.

### 2. **Comparaison temporelle (Graphiques)**
- Visualisation de l'évolution du prix moyen au fil du temps.
- Comparaison côte à côte de deux régions sélectionnées.
- Échelle synchronisée (axe Y fixe) entre les graphiques pour garantir une comparaison visuelle honnête et efficace.

### 3. **Section documentaire (Markdown)**
- Présentation pédagogique des concepts Dash (Layout, Callbacks).
- Navigation fluide via un composant Accordion pour une expérience utilisateur moderne.

---

## 🛠️ Installation

### Prérequis
- Python 3.8 ou supérieur
- [Poetry](https://python-poetry.org/) ou un autre gestionnaire d'environnement Python

### Étapes d'installation

1. **Cloner le dépôt :**
   ```bash
   git clone <votre-url-depot>
   cd DASH_CONTROLE_160326
   ```

2. **Installer les dépendances :**
   ```bash
   poetry install
   ```

3. **Lancer l'application :**
   ```bash
   poetry run python app.py
   ```

---

## 📂 Architecture du projet

Le projet suit une organisation modulaire, séparant les interfaces (Layouts) de la logique interactive (Callbacks) :
```bash
DASH_CONTROLE_160326/
│
├── pages/                  ← Modules des pages de l'application [cite: 62]
│   ├── table.py            ← Layout de la Page 1 (Données) [cite: 71]
│   ├── table_cb.py         ← Logique des filtres du tableau 
│   ├── compare.py          ← Layout de la Page 2 (Comparaison) [cite: 160]
│   ├── compare_cb.py       ← Logique des graphiques comparatifs [cite: 178]
│   └── markdown.py         ← Page 3 (Documentation Accordion) [cite: 182]
│
├── assets/                 ← Ressources statiques (CSS, Images, MD) [cite: 65]
│   ├── dash.jpg            ← Image de bannière pour la page Markdown
│   ├── expli1.md           ← Contenu : Accueil
│   ├── expli2.md           ← Contenu : Layout [cite: 186]
│   └── expli3.md           ← Contenu : CallBack [cite: 197]
│
├── datas/                  ← Données sources [cite: 66]
│   └── avocado.csv         ← Jeu de données des ventes d'avocats [cite: 21]
│
├── app.py                  ← Point d'entrée principal (Multi-pages) [cite: 61, 209]
├── pyproject.toml          ← Configuration UV et dépendances
└── README.md               ← Vous êtes ici ! [cite: 67]
```

🚀 Utilisation
L'interface se divise en trois sections majeures accessibles via la barre de navigation:
+1

Affichage des données : Utilisez les menus déroulants pour isoler une région spécifique ou un type d'avocat. Le tableau se met à jour instantanément.

Comparaison entre régions : Sélectionnez deux régions différentes. Observez que les deux graphiques utilisent les mêmes bornes de prix pour identifier immédiatement laquelle est la plus chère.

Aide en ligne : Consultez la documentation interactive pour comprendre comment l'application a été construite techniquement.