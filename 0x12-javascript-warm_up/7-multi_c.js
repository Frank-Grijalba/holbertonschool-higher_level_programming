#!/usr/bin/node
const argv = process.argv;
const ocurrences = parseInt(argv[2]);
let i = 0;
if (isNaN(ocurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < ocurrences; i++) {
    console.log('C is fun');
  }
}
