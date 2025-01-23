// add const fs to access the file system
const fs = require('fs');

// create a function to read a file asynchronously
function countStudents(path) {
  // use fs.readFile to read the file asynchronously
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // treat the data
      const lines = data.trim().split('\n').filter((line) => line); // remove empty lines
      const students = {};
      let NUMBER_OF_STUDENTS = 0;

      // Ignore the header row
      for (let i = 1; i < lines.length; i++) {
        const [firstname, lastname, age, field] = lines[i].split(',');
        if (field) {
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
          NUMBER_OF_STUDENTS++;
        }
      }

      // print the results
      const output = [];
      output.push(`Number of students: ${NUMBER_OF_STUDENTS}`);
      for (const field in students) {
        output.push(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
      }

      resolve(output.join('\n')); // Retourne les résultats formatés
    });
  });
}

module.exports = countStudents;
