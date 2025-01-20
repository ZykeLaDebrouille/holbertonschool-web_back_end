#!/bin/bash

# Création du dossier principal
mkdir -p Node_JS_basic

# Création des fichiers de base
touch Node_JS_basic/0-console.js
touch Node_JS_basic/1-stdin.js
touch Node_JS_basic/2-read_file.js
touch Node_JS_basic/3-read_file_async.js
touch Node_JS_basic/4-http.js
touch Node_JS_basic/5-http.js
touch Node_JS_basic/6-http_express.js
touch Node_JS_basic/7-http_express.js

# Création de la structure full_server
mkdir -p Node_JS_basic/full_server/controllers
mkdir -p Node_JS_basic/full_server/routes

# Création des fichiers full_server
touch Node_JS_basic/full_server/utils.js
touch Node_JS_basic/full_server/controllers/AppController.js
touch Node_JS_basic/full_server/controllers/StudentsController.js
touch Node_JS_basic/full_server/routes/index.js
touch Node_JS_basic/full_server/server.js

# Création des fichiers de configuration
touch Node_JS_basic/package.json
touch Node_JS_basic/babel.config.js
touch Node_JS_basic/.eslintrc.js
touch Node_JS_basic/database.csv

# Ajout des permissions d'exécution
chmod +x Node_JS_basic/*.js
chmod +x Node_JS_basic/full_server/*.js
chmod +x Node_JS_basic/full_server/controllers/*.js
chmod +x Node_JS_basic/full_server/routes/*.js

echo "Structure du projet créée avec succès !"
