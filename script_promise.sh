#!/bin/bash

# Créer le répertoire du projet
mkdir -p ES6_promise

# Créer les fichiers de tâches
for i in {0..9}
do
    echo "// Task $i" > ES6_promise/$i-promise.js
    echo "// Main file for Task $i" > ES6_promise/$i-main.js
done

# Renommer certains fichiers spécifiques
mv ES6_promise/1-promise.js ES6_promise/1-promise.js
mv ES6_promise/2-promise.js ES6_promise/2-then.js
mv ES6_promise/3-promise.js ES6_promise/3-all.js
mv ES6_promise/4-promise.js ES6_promise/4-user-promise.js
mv ES6_promise/5-promise.js ES6_promise/5-photo-reject.js
mv ES6_promise/6-promise.js ES6_promise/6-final-user.js
mv ES6_promise/7-promise.js ES6_promise/7-load_balancer.js
mv ES6_promise/8-promise.js ES6_promise/8-try.js
mv ES6_promise/9-promise.js ES6_promise/9-try.js

# Créer utils.js
echo "// Utility functions" > ES6_promise/utils.js

echo "Files created successfully!"
