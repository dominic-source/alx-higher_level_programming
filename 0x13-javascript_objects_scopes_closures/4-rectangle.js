#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      let x = '';
      for (j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    const hold = this.width;
    this.width = this.height;
    this.height = hold;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
