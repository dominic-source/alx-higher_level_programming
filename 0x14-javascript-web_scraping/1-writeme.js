#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, { encoding: 'utf-8' }, (err, fd) => {
  if (err) {
    console.log(err);
  }
});
