#!/usr/bin/node

let first;
let second;
first = second = -(Number.MAX_VALUE);
const arr = process.argv;

if (arr.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
    if (arr[i] && arr[i] > first) {
      second = first;
      first = arr[i];
    }
    if (arr[i] && arr[i] > second && arr[i] < first) {
      second = arr[i];
    }
  }
  console.log(second);
}
