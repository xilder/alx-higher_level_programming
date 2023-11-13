#!/usr/bin/node

const num = parseInt(process.argv[2]);
let total = 1;

if (num) {
  for (let i = 1; i <= num; i++) {
    total *= i;
  }
  console.log(total);
} else {
  console.log(1);
}
