#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
