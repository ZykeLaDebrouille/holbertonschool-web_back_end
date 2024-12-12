# **Projet : Pagination avec Python**

## **Description**
Ce projet explore les principes de la pagination pour les bases de données ou API. Tu apprendras à :
- Paginer un dataset avec des paramètres simples (`page`, `page_size`).
- Gérer la pagination avec des métadonnées hypermédia.
- Implémenter une pagination résiliente face à des suppressions de données.

Les concepts et techniques utilisés sont des fondations pour concevoir des **API RESTful performantes** et maintenables.

---

# **Contenu du projet**

Le projet est divisé en plusieurs étapes, chacune avec ses objectifs spécifiques :

1. **Helper Function**
   - Création d'une fonction `index_range` pour calculer les index de début et de fin pour la pagination.
2. **Simple Pagination**
   - Implémentation d'une pagination de base avec validation des entrées.
3. **Hypermedia Pagination**
   - Ajout de métadonnées pour enrichir la pagination.
4. **Deletion-Resilient Pagination**
   - Implémentation d'une pagination robuste qui gère les suppressions dans les datasets.

---

## **Prérequis**

- **Python** : Version 3.9 ou supérieure.
- **Système d'exploitation** : Testé sur Ubuntu 20.04 LTS.
- **Dépendances Python** :
  - `pycodestyle` (pour le respect des normes de style).
  
Pour installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## **Exigences**

- **Respect des normes de style** : Code conforme à `pycodestyle==2.5.*`.
- **Documentation** :
  - Modules, classes et fonctions documentés (minimum une phrase claire par élément).
  - Exemple :

    ```python
    """
    Cette fonction calcule l'index de début et de fin pour une pagination.
    """
    ```

- **Type annotations** : Toutes les fonctions doivent inclure des annotations de type.
- **Fichiers de test** : Chaque tâche doit avoir ses propres tests unitaires dans le dossier `tests`.

---

## **Organisation du projet**

```mark
pagination/
├── data/
│   └── Popular_Baby_Names.csv       # Dataset utilisé pour les tests
├── src/
│   ├── 0-simple_helper_function.py # Fonction helper
│   ├── 1-simple_pagination.py      # Pagination simple
│   ├── 2-hypermedia_pagination.py  # Pagination hypermédia
│   ├── 3-hypermedia_del_pagination.py # Pagination résiliente
│   └── __init__.py                 # Pour rendre le module importable
├── tests/
│   ├── test_0_simple_helper_function.py # Tests pour la tâche 0
│   ├── test_1_simple_pagination.py      # Tests pour la tâche 1
│   ├── test_2_hypermedia_pagination.py  # Tests pour la tâche 2
│   ├── test_3_hypermedia_del_pagination.py # Tests pour la tâche 3
│   └── __init__.py
├── README.md                        # Documentation du projet
└── requirements.txt                 # Dépendances Python
```

---

## **Comment exécuter le projet**

### 1. **Initialisation**

Clone le dépôt :

```bash
git clone <URL_DU_DEPOT>
cd pagination
```

Installe les dépendances :

```bash
pip install -r requirements.txt
```

### 2. **Lancer les tests**

Pour vérifier que tout fonctionne :

```bash
python -m unittest discover tests/
```

---

## **Exemple d'utilisation**

### **Helper Function**

Code :

```python
from src.0_simple_helper_function import index_range

print(index_range(1, 10))  # (0, 10)
print(index_range(2, 10))  # (10, 20)
```

### **Pagination simple**

Code :

```python
from src.1_simple_pagination import Server

server = Server()
print(server.get_page(1, 5))  # Première page avec 5 résultats
```

---

## **Ressources utilisées**

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

---

## **Auteurs**

- **Zyke !**
- Projet réalisé dans le cadre de [Holberton School](https://www.holbertonschool.com).

---
