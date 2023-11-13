#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

if (num) {
  console.log(factorial(num));
} else {
  console.log(1);
}
