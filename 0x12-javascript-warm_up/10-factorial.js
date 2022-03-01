#!/usr/bin/node
const { argv } = require('process');
const factorial = (n) => {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
};
const number = Number(argv[2]);
console.log(factorial(number));
