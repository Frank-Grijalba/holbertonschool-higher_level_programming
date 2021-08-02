#!/usr/bin/node
const argv = process.argv;
const number = parseInt(argv[2]);
const draw = 'x';
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log(draw.repeat(number));
  }
}
