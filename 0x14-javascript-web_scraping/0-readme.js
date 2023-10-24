#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
