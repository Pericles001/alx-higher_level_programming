#!/usr/bin/node
const { argv } = require('process');
const converted = Number(argv[2]);
if (isNaN(converted)) { console.log('Not a number'); } else { console.log(`My number: ${converted}`); }
