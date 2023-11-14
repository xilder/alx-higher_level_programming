#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};
const values = Object.entries(dict);

values.forEach(([key, value]) => {
  if (value in newDict) {
    newDict[value].push(key.toString());
  } else {
    newDict[value] = [];
    newDict[value].push(key.toString());
  }
});

console.log(newDict);
