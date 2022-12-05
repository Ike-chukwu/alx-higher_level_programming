#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(num));
