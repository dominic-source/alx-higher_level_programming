#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    const cha = c !== undefined ? c : 'X';
    let i;
    let j;
    for (i = 0; i < this.size; i++) {
      let x = '';
      for (j = 0; j < this.size; j++) {
        x += cha;
      }
      console.log(x);
    }
  }
}
module.exports = Square;
