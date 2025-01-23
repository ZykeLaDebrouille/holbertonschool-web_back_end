const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.write('Hello Holberton School!');
  res.end();
});

app.get('/students', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain',
  });
  res.write('Hello Holberton students!');
  if (process.argv.length > 2) {
    const csvFile = process.argv[2];
    const output = 'This is the list of our students\n';

    const originalLog = console.log;
    let capturedOutput = '';
    console.log = (message) => {
      capturedOutput += `${message}\n`;
    };

    countStudents(csvFile)
      .then(() => {
        console.log = originalLog;
        res.write(output);
        res.write(capturedOutput.trim());
        res.end();
      });
  }
});

app.listen(port);

module.exports = app;
