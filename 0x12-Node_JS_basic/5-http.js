const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  switch (req.url) {
    case '/':
      res.writeHead(200);
      res.end('Hello Holberton School!');
      break;
    case '/students':
      res.writeHead(200);
      res.write('This is the list of our students\n');
      countStudents(process.argv[2])
        .then((data) => {
          res.end(data);
        })
        .catch((error) => {
          res.end(error.message);
        });
      break;
    default:
      res.writeHead(404);
      res.end(JSON.stringify({ error: 'Resource not found' }));
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;