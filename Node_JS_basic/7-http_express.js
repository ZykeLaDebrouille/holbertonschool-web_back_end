import express from 'express';
import { promises as fs } from 'fs';

// Create an Express application
const app = express();

/**
 * Reads a CSV file asynchronously and returns an object of student arrays grouped by field.
 * @param {string} path - The path to the CSV file.
 * @returns {Promise} - A promise that resolves with an object of student arrays grouped by field, or rejects with an error.
 */
const readDatabase = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    const [header, ...students] = lines;
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

// Route for the homepage
app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

// Route to get all students
app.get('/students', async (req, res) => {
  try {
    const database = process.argv[2]; // Get the database file path from command-line arguments
    if (!database) {
      throw new Error('Cannot load the database');
    }

    const studentsByField = await readDatabase(database);

    let responseText = 'This is the list of our students\n';
    for (const [field, students] of Object.entries(studentsByField)) {
      responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
    }

    res.status(200).send(responseText.trim()); // Remove the last newline
  } catch (error) {
    res.status(500).send('Cannot load the database');
  }
});

// Start the server on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for testing
export default app;
