#!/usr/bin/node

const num = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add(a, b) {
	console.log(a + b);
}

if (num && num2) {
  add(num, num2);
  } else {
  console.log('NaN');
}
