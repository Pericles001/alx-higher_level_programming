#!/usr/bin/node
const { argv } = require('process');
const factorial = (n) => {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
};
const number = Number(argv[2]);
console.log(factorial(number));
