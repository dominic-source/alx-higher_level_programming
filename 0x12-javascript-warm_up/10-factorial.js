#!/usr/bin/node

function factorial (num) {
  if (num < 1) return (1);
  return (num * factorial(num - 1));
}

const pros = Number(process.argv[2]);
if (!pros) console.log('1');
else {
  console.log(factorial(pros));
}
