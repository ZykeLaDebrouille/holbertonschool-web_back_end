
# Python Async Comprehension

![Python Async](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png)

Bienvenue dans le projet **Python Async Comprehension** ! 🚀 Ici, nous explorons les concepts d'asynchronisme en Python, notamment les **générateurs asynchrones**, **les compréhensions asynchrones**, et bien plus. Prépare-toi à devenir un expert des coroutines. 🥷

---

## 🧠 Objectifs pédagogiques

À la fin de ce projet, tu seras capable de :

- Écrire un **générateur asynchrone**.
- Utiliser les **compréhensions asynchrones** pour collecter des données asynchrones.
- Annoter correctement les coroutines et générateurs.

---

## 🛠️ Configuration et exigences

### Outils requis

- Éditeurs recommandés : `vi`, `vim`, `emacs`.
- Système : **Ubuntu 20.04 LTS** avec Python **3.9**.

### Style et bonnes pratiques

- Respecter la norme **Pycodestyle** (version 2.5.x).
- Documentation obligatoire pour :
  - Les modules.
  - Les fonctions/coroutines.
- Les **type annotations** sont obligatoires pour toutes les fonctions et coroutines.
- Tous les fichiers doivent se terminer par une nouvelle ligne.

---

## 🚀 Contenu du projet

### Tâche 0 : Async Generator
>
> Fichier : `0-async_generator.py`

Crée une coroutine `async_generator` qui génère **10 valeurs asynchrones**, avec une pause d'1 seconde entre chaque valeur.

#### Exemple pédagogique

```python
# Imagine un générateur classique Python
def simple_generator():
    for i in range(5):
        yield i

# En mode asynchrone, cela pourrait ressembler à ceci :
import asyncio

async def async_example_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulation d'une opération lente
        yield i

# Exemple d'utilisation
# Cette boucle permet de récupérer les valeurs une par une
async def demo():
    async for value in async_example_generator():
        print(value)

# Appel de la coroutine
# asyncio.run(demo())
```

---

### Tâche 1 : Async Comprehensions
>
> Fichier : `1-async_comprehension.py`

Crée une coroutine `async_comprehension` qui collecte **10 valeurs générées par un générateur asynchrone** en utilisant une **compréhension asynchrone**.

#### Exemple pédagogique 1

```python
# Imagine une liste générée normalement
def generate_list():
    return [x for x in range(10)]

# En mode asynchrone, cela pourrait ressembler à :
async def async_comprehension_example():
    # Utilisation d'une compréhension asynchrone
    return [value async for value in async_example_generator()]

# Exemple d'utilisation
async def demo():
    results = await async_comprehension_example()
    print(results)

# asyncio.run(demo())
```

---

### Tâche 2 : Run time for four parallel comprehensions
>
> Fichier : `2-measure_runtime.py`

Crée une coroutine `measure_runtime` qui exécute **4 coroutines asynchrones en parallèle** et mesure le **temps total d'exécution**.

#### Exemple pédagogique 2

```python
# Imagine que tu as plusieurs tâches lentes
async def slow_task(index):
    await asyncio.sleep(2)  # Simule une tâche de 2 secondes
    return f"Task {index} done"

# Exécuter plusieurs tâches en parallèle
async def parallel_execution_example():
    tasks = [slow_task(i) for i in range(4)]
    results = await asyncio.gather(*tasks)  # Lancer toutes les tâches
    print(results)

# Exemple d'utilisation pour mesurer le temps
import time
async def measure_time_example():
    start = time.time()
    await parallel_execution_example()
    print(f"Time elapsed: {time.time() - start} seconds")

# asyncio.run(measure_time_example())
```

---

## 📂 Organisation du repo

``` mark
holbertonschool-web_back_end/
├── python_async_comprehension/
│   ├── 0-async_generator.py
│   ├── 1-async_comprehension.py
│   ├── 2-measure_runtime.py
│   └── README.md
```

---

## 🎯 Objectif final

Avec ces bases, tu seras prêt·e à comprendre et implémenter des concepts avancés d'asynchronisme en Python. Bonne exploration ! 🚀

---
