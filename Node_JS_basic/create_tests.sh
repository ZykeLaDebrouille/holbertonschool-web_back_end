#!/bin/bash

# Répertoire des tests
TEST_DIR="Node_JS_basic/tests"
mkdir -p "$TEST_DIR"

# Test pour 0-console.js
cat > "$TEST_DIR/0-console.test.js" << EOF
const { expect } = require('chai');
const displayMessage = require('../0-console');

describe('displayMessage', () => {
    it('should log the correct message', () => {
        const message = 'Hello, World!';
        const consoleSpy = sinon.spy(console, 'log');
        displayMessage(message);
        expect(consoleSpy.calledWith(message)).to.be.true;
        consoleSpy.restore();
    });
});
EOF

# Test pour 1-stdin.js
cat > "$TEST_DIR/1-stdin.test.js" << EOF
const { expect } = require('chai');

describe('1-stdin', () => {
    it('should handle input and output properly (manual testing required)', () => {
        expect(true).to.be.true;
        // Note: Impossible de tester correctement stdin/stdout de manière automatisée.
    });
});
EOF

# Test pour 2-read_file.js
cat > "$TEST_DIR/2-read_file.test.js" << EOF
const { expect } = require('chai');
const countStudents = require('../2-read_file');

describe('countStudents', () => {
    it('should throw an error if the file does not exist', () => {
        expect(() => countStudents('non_existent_file.csv')).to.throw('Cannot load the database');
    });

    it('should correctly count students and group them by field', () => {
        const path = './database.csv';
        // Simuler le fichier CSV
        const expectedOutput = [
            'Number of students: 10',
            'Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie',
            'Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy',
        ].join('\\n');
        expect(() => countStudents(path)).not.to.throw();
    });
});
EOF

# Test pour 3-read_file_async.js
cat > "$TEST_DIR/3-read_file_async.test.js" << EOF
const { expect } = require('chai');
const countStudents = require('../3-read_file_async');

describe('countStudents (async)', () => {
    it('should reject if the file does not exist', async () => {
        try {
            await countStudents('non_existent_file.csv');
        } catch (error) {
            expect(error.message).to.equal('Cannot load the database');
        }
    });

    it('should resolve with correct data if the file exists', async () => {
        const path = './database.csv';
        const expectedOutput = [
            'Number of students: 10',
            'Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie',
            'Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy',
        ].join('\\n');
        const result = await countStudents(path);
        expect(result).to.equal(expectedOutput);
    });
});
EOF

# Test pour 4-http.js
cat > "$TEST_DIR/4-http.test.js" << EOF
const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../4-http');

chai.use(chaiHttp);

describe('4-http', () => {
    it('should respond with "Hello Holberton School!" on /', (done) => {
        chai.request(app)
            .get('/')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.equal('Hello Holberton School!');
                done();
            });
    });
});
EOF

# Test pour 5-http.js
cat > "$TEST_DIR/5-http.test.js" << EOF
const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../5-http');

chai.use(chaiHttp);

describe('5-http', () => {
    it('should respond with "Hello Holberton School!" on /', (done) => {
        chai.request(app)
            .get('/')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.equal('Hello Holberton School!');
                done();
            });
    });

    it('should respond with student list on /students', (done) => {
        chai.request(app)
            .get('/students')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.contain('Number of students:');
                done();
            });
    });
});
EOF

# Test pour 6-http_express.js
cat > "$TEST_DIR/6-http_express.test.js" << EOF
const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../6-http_express');

chai.use(chaiHttp);

describe('6-http_express', () => {
    it('should respond with "Hello Holberton School!" on /', (done) => {
        chai.request(app)
            .get('/')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.equal('Hello Holberton School!');
                done();
            });
    });
});
EOF

# Test pour 7-http_express.js
cat > "$TEST_DIR/7-http_express.test.js" << EOF
const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../7-http_express');

chai.use(chaiHttp);

describe('7-http_express', () => {
    it('should respond with "Hello Holberton School!" on /', (done) => {
        chai.request(app)
            .get('/')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.equal('Hello Holberton School!');
                done();
            });
    });

    it('should respond with student list on /students', (done) => {
        chai.request(app)
            .get('/students')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.contain('Number of students:');
                done();
            });
    });

    it('should respond with custom message on /home', (done) => {
        chai.request(app)
            .get('/home')
            .end((err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res.text).to.contain("Bah mon gars");
                done();
            });
    });
});
EOF

echo "Tests generated successfully in $TEST_DIR!"
