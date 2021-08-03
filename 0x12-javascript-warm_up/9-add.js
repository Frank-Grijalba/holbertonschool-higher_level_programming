#!/usr/bin/node
const argv = process.argv;
const number1 = parseInt(argv[2]);
const number2 = parseInt(argv[3]);
if (isNaN(number1) || isNaN(number2)) {
  console.log('Not is a Number');
} else {
  function add (a, b) { return a + b; }
  console.log(add(number1, number2));
}
