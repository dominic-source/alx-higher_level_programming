#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const dict = {};
    const data = JSON.parse(body);
    data.forEach((item, index) => {
      if (item.completed === true) {
        dict[item.userId] === undefined ? dict[item.userId] = 1 : dict[item.userId] += 1;
      }
    });
    console.log(dict);
  }
});
