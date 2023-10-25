#!/usr/bin/node

const process = require('process');
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

async function handleRequest (urls) {
  for (let index = 0; index < urls.length; index++) {
    const result = urls[index];
    try {
      const body2 = await new Promise((resolve, reject) => {
        request.get(result, (err2, res2, body2) => {
          if (err2) {
            reject(err2);
          } else if (res2.statusCode === 200) {
            resolve(body2);
          }
        });
      });
      const newdata = JSON.parse(body2).name;
      console.log(newdata);
    } catch (err) {
      console.error(err);
    }
  }
}

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    handleRequest(JSON.parse(body).characters);
  }
});
