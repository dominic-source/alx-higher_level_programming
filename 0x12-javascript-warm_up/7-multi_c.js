#!/usr/bin/node

const pros = Number(process.argv[2]);
if (!pros) console.log('Missing number of occurrences');
else {
  let i = 0;
  while (i < pros) {
    console.log('C is fun');
    i++;
  }
}
