#!/usr/bin/node

/*
 * Represents a Square
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
    console.log(line);
    }
}

module.exports = Square;
