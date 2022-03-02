#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    let line = '';
    for (let i = 0; i < this.height; i++) {
      line += 'X';
      console.log(line.repeat(this.width));
    }
  }
};
