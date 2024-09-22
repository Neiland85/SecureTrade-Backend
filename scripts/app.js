// app.js

const express = require('express');
const app = express();

// Middleware para parsear JSON
app.use(express.json());

// Ruta de ejemplo
app.get('/', (req, res) => {
  res.send('Hello, lovely world! Stay tuned today i will fuck your anus on wallstreet!! Take care honey, peace!');
});

// app.use('/api', require('./routes/api'));

module.exports = app;
