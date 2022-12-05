#!/usr/bin/node

let i = 0;
const num = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
