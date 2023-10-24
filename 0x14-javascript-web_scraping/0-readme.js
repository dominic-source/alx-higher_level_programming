#!/usr/bin/node

const process = require('node:process');
const fs = require('node:fs');
const filename = process.argv[2];

fs.readFile(filename, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
