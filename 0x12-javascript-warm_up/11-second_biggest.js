#!/usr/bin/node
const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  const array1 = argv.slice(2);
  array1.sort(function (a, b) {
    return b - a;
  });
  console.log(array1[1]);
}
