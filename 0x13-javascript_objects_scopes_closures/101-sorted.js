#!/usr/bin/node
const { dict } = require('./101-data.js');

const newdict = {};
let key;
for (key in dict) {
  const nkey = dict[key];
  if (newdict[nkey]) newdict[nkey].push(key);
  else newdict[nkey] = [key];
}
console.log(newdict);
