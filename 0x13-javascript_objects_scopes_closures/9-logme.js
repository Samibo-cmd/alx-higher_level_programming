#!/usr/bin/node
let numbArg = 0;

exports.logMe = function (item) {
  console.log(numbArg + ': ' + item);
  numbArg++;
};
