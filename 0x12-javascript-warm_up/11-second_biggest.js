#!/usr/bin/node

const pros = process.argv;
if (pros.length === 0 || pros.length === 1) {
  console.log(0);
} else {
  let i = 0;
  let j = 0;
  let k;
  let val;
  for (k = 0; k < pros.length; k++) {
    val = Number(pros[k]);
    if (val > i) {
      j = i;
      i = val;
    } else if (val > j) {
      j = val;
    }
  }
  console.log(j);
}
