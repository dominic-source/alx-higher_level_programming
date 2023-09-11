#!/usr/bin/node

const pros = Number(process.argv[2]);
if (!pros) console.log('1');
else {
  factorial(pros);
}
