#!/usr/bin/node

if (process.argv.length >= 3) {
  const res = process.argv[2].concat(' is ', process.argv[3]);
  console.log(res);
} else {
  const res = 'undefined'.concat(' is ', process.argv[3]);
  console.log(res);
}
