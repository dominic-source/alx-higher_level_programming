#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
