export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100); // Met à jour la quantité à 100 si elle est initialement à 1
    }
  }

  return map;
}
