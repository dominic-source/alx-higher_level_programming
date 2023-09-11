#!/usr/bin/node

const pros = process.argv.slice(2);
if (pros.length === 1) {
  console.log('Argument found');
} else if (pros.length === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
