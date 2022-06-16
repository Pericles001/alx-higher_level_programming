#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined || !(Number(argv[2]))) {
  console.log('Missing size');
} else {
  const rip = 'X'.repeat(argv[2]);
  for (let i = 0; i < argv[2]; i++) {
    console.log(rip);
  }
}