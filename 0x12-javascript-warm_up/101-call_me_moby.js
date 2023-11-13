#!/usr/bin/node

exports.callMeMoby = (x, myFunc) => {
  for (let i = 0; i < x; i++) {
    myFunc();
  }
};
