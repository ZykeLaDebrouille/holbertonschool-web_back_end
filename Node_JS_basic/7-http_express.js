const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (error, data) => {
            if (error) {
                reject(new Error('Cannot load the database'));
                return;
            }

            let output = '';
            const lines = data.trim().split('\n').filter(line => line);
            const students = {};
            let numberOfStudents = 0;

            for (let i = 1; i < lines.length; i++) {
                const [firstname, lastname, age, field] = lines[i].split(',');
                if (field) {
                    if (!students[field]) {
                        students[field] = [];
                    }
                    students[field].push(firstname);
                    numberOfStudents++;
                }
            }

            output += `Number of students: ${numberOfStudents}\n`;
            for (const field in students) {
                output += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
            }

            resolve(output);
        });
    });
}

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

app.listen(port);

module.exports = app;
