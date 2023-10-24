#!/usr/bin/node

const process = require('process');
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body).characters;
    data.forEach((result, index) => {
      request.get(result, (err2, res2, body2) => {
        if (err2) {
          console.log(err2);
        } else if (res2.statusCode === 200) {
          const newdata = JSON.parse(body2).name;
          console.log(newdata);
        }
      });
    });
  }
});
