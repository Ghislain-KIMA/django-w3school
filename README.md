# 🎾 My Tennis Club — Gestion des Membres (Django)

Application web développée avec **Django** pour gérer l'annuaire des membres d'un club de tennis, incluant la génération automatique de slugs SEO-friendly, des fiches détaillées, la gestion des fichiers statiques et une commande d'administration personnalisée pour peupler la base de données.

---

## 🛠️ Technologies & Outils

* **Langage :** Python 3.14+
* **Framework Web :** Django
* **Base de données :** PostgreSQL (Production)
* **Environnement :** Conda / Miniconda

---

## 📁 Structure du Projet

```text
.
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── my_tennis_club/             # Configuration principale du projet
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── members/                    # Application de gestion des membres
│   ├── models.py               # Modèle Member (champs, slugs)
│   ├── views.py                # Vues applicatives
│   ├── urls.py                # Routage (ex: members/<slug:slug>/)
│   ├── admin.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_members.py # Commande personnalisée d'injection en masse de membres
│   ├── migrations/
│   ├── static/                 # Fichiers CSS spécifiques aux membres
│   └── templates/
│       └── members/
│           ├── home.html
│           ├── member.html
│           └── members.html
│
├── mystaticfiles/              # Styles globaux (myglobal.css, mystyles.css)
└── templates/                  # Templates globaux
    ├── base.html
    ├── 404.html
    └── 500.html
```

---

## 🚀 Guide de Démarrage Rapide

### 1. Activer l'environnement Conda

```bash
conda activate django-w3school-tp
```

### 2. Appliquer les migrations de base de données

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Insérer les membres de test (Seed)

Exécute la commande personnalisée pour générer automatiquement les membres et leurs slugs :

```bash
python manage.py seed_members
```

### 4. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application sera accessible sur `http://127.0.0.1:8000/`.

---

## 🌐 Endpoints & Navigation

| URL                  | Template         | Description                                                  |
| -------------------- | ---------------- | ------------------------------------------------------------ |
| `/`                | `home.html`    | Page d'accueil du club                                       |
| `/members/`        | `members.html` | Liste complète et cliquable des membres                     |
| `/members/<slug>/` | `member.html`  | Fiche détaillée d'un membre identifié par son slug unique |

---

## ⚙️ Commandes Utiles

* **Générer les fichiers statiques de production :**

```bash
python manage.py collectstatic
```

* **Accéder au shell Django pour manipuler les données :**

```bash
python manage.py shell
```

```

---

<ElicitationsGroup message="Souhaites-tu effectuer d'autres ajustements sur ton projet ?">
  <Elicitation label="Ajouter un fichier .gitignore approprié au projet" query="Génère un fichier .gitignore complet adapté à ce projet Django, VS Code et Conda."/>
  <Elicitation label="Créer un script d'initialisation rapide du projet" query="Crée un script bash d'une seule ligne pour automatiser les migrations, le seed et le lancement du serveur."/>
</ElicitationsGroup>
```


## Commandes de déployement sur render

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate  # L'option `--noinput` permet d'exécuter `collectstatic` en mode automatique sans demander de confirmation dans le terminal de Render.
