const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2]; // Récupère le nom du fichier en argument

    res.write('This is the list of our students:\n');

    countStudents(database)
      .then((data) => {
        res.end(data); // Envoie la liste des étudiants au client
      })
      .catch((error) => {
        res.end(`Error: ${error.message}`); // Envoie l'erreur au client
      });
  }
});

app.listen(1245);

module.exports = app;
