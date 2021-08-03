#!/usr/bin/node
const argv = process.argv;
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log(1);
} else {
  function factorial (n) {
    if (n <= 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  };
  console.log(factorial(number));
}
