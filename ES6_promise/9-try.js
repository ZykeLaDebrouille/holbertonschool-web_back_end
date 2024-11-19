export default function guardrail(mathFunction) {
  const resulat = []; // Créer un tableau pour stocker les résultats

  try {
    // Essayer d'exécuter la fonction mathématique et ajouter le résultat à la resulat
    const result = mathFunction();
    resulat.push(result);
  } catch (error) {
    // Si une erreur est lancée, ajouter le message d'erreur à la resulat
    resulat.push(`Error: ${error.message}`);
  } finally {
    // Dans tous les cas, ajouter le message de traitement à la resulat
    resulat.push('Guardrail was processed');
  }

  return resulat;
}
