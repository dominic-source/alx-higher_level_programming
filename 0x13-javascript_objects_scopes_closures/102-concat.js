#!/usr/bin/node

const fs = require('fs');

const filenames = process.argv;
const file1 = filenames[2];
const file2 = filenames[3];
const file3 = filenames[4];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.log(err);
      return;
    }
    const concat = data1 + data2;
    fs.writeFile(file3, concat, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
});
