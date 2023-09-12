#!/usr/bin/node

const pros = Number(process.argv[2]);
if (!pros) console.log('Missing size');
else if (pros > 1) {
  let i = 0;
  let j = 0;
  while (i < pros) {
    let str = '';
    for (j = 0; j < pros; j++) str += 'x';
    console.log(str);
    i++;
  }
}
