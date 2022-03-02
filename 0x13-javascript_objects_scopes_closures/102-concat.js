#!/usr/bin/node
const fs = require('fs');
const src1 = fs.readFileSync(process.argv[2], 'utf8');
const src2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], src1 + src2);
