#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let counter = 0;
    const data = JSON.parse(body).results;
    data.forEach((result, index) => {
      result.characters.forEach((character, idx) => {
        if (character.endsWith('18/')) {
          counter += 1;
        }
      });
    });
    console.log(counter);
  }
});
