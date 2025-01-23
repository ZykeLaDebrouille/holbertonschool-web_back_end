const express = require('express');
const fs = require('fs').promises;
const app = express();

const countStudents = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Ignore la première ligne (en-tête)

    if (students.length === 0) {
      throw new Error('Cannot load the database');
    }

    const fields = {};
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    console.log(`Number of students: ${students.length}`);
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

    return Promise.resolve();
  } catch (error) {
    return Promise.reject(new Error('Cannot load the database'));
  }
};

module.exports = countStudents;


app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const database = process.argv[2];
  try {
    const output = await countStudents(database);
    res.send(`This is the list of our students\n${output}`);
  } catch (error) {
    res.send(error.message);
  }
});

app.get('/home', async (req, res) => {
  res.send("Bah mon gars tu t'es perdu ou quoi ? Ici c'est chez moi !\n");
});

app.listen(1245);

module.exports = app;
