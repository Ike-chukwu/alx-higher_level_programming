#!/usr/bin/node

const size = process.argv[2];
let charc = '';
if (process.argv.length < 3 || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    charc = '';
    for (let j = 0; j < size; j++) charc += 'X';
    console.log(charc);
  }
}
