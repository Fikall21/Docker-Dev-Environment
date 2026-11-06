const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Node.js Frontend Service Running Successfully!');
});

app.listen(port, () => {
  console.log(`Frontend app listening at http://localhost:${port}`);
});