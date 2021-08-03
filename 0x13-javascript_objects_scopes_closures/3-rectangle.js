#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const draw = 'X';
    for (const i = 0; i < this.height; i++) {
      console.log(draw.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
