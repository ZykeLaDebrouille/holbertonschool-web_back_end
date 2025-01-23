const express = require('express');
const fs = require('fs').promises;
const app = express();
const port = 1245;

// Function to count students and group them by field (program)
const countStudents = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Ignore the first line (header)

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

    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

// Route for the root path
app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

// Route for the /students path
app.get('/students', async (req, res) => {
  const databaseFile = process.argv[2]; // Database file passed as argument

  if (!databaseFile) {
    return res.status(400).send('Database file is required');
  }

  try {
    const fields = await countStudents(databaseFile);
    const totalStudents = Object.values(fields).flat().length; // Flatten the array and count
    res.type('text/plain');
    res.send(`This is the list of our students\nNumber of students: ${totalStudents}\n` +
      Object.entries(fields).map(([field, names]) => 
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`).join('\n'));
  } catch (error) {
    res.status(500).send('Error reading the database');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

module.exports = app;
