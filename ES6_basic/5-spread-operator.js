export default function concatArrays(array1, array2, string) {
  const concatenatedArray = array1.concat(array2);

  for (let i = 0; i < string.length; i += 1) {
    concatenatedArray.push(string[i]);
  }

  return concatenatedArray;
}
