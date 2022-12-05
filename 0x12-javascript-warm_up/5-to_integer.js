#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(num));
}
