for i in {0..12}
do
    filename="${i}-main.js"
    
    # Vérifier si le fichier existe déjà
    if [ ! -f "$filename" ]; then
        # Créer le fichier avec un contenu de base
        echo "// ${i}-main.js" > "$filename"
        echo "import { /* importez vos fonctions ici */ } from './${i}-${task_name}.js';" >> "$filename"
        echo "" >> "$filename"
        echo "console.log(/* appelez vos fonctions ici */);" >> "$filename"
        
        echo "Fichier $filename créé."
    else
        echo "Le fichier $filename existe déjà."
    fi
done

echo "Création des fichiers main.js terminée."