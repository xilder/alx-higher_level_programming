#!/usr/bin/node

exports.addMeMaybe = (x, myFunc) => {
  myFunc(++x);
};
