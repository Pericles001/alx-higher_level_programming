#!/usr/bin/node
const { argv } = require('process');
if (argv[2] === undefined && argv[3] === undefined) { console.log('Undefined is undefined'); } else if (argv[3] === undefined) { console.log(argv[2] + ' is undefined'); } else { console.log(argv[2] + ' is ' + argv[3]); }
