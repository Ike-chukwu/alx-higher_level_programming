#!/usr/bin/node

const size = process.argv.length;

if (size <= 3) {
  console.log(0);
} else {
  const newA = process.argv.map(Number);
  newA.slice(2, size);
  newA.sort((a, b) => a - b);
  console.log(newA[newA.length - 2]);
}
