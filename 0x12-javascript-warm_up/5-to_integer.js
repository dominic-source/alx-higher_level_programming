#!/usr/bin/node

const pros = process.argv[2];
const num = Number(pros);
if (num) console.log('My number: ' + num);
else console.log('Not a number');
