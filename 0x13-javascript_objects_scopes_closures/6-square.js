#!/usr/bin/node

/*
 * Represents a Square
 */

const PrevSquare = require('./5-square');

class Square extends PrevSquare {

  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += ch;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
