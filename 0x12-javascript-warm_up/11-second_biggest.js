#!/usr/bin/node

const pros = process.argv;
if (pros.length === 0 || pros.length === 1) {
  console.log(0);
}
else {
  let i = 0;
  let j = 0;
  let k;
  for (k = 0; k < pros.length; k++) {
    if (pros[k] > i) {
      j = i;
      i = pros[k];
    } else if (pros[k] > j) {
      j = pros[k];
    }
  }
}
