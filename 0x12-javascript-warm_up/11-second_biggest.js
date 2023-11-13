#!/usr/bin/node

let first;
let second;
first = second = -(Number.MAX_VALUE);
const arr = process.argv;

if (arr.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] < first) {
      second = arr[i];
    }
  }
  console.log(second);
}
