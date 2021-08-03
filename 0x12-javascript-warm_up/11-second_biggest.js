#!/usr/bin/node
const argv = process.argv;

const secondBiggest = (array) => {
  const array1 = array.slice(2);
  array1.sort(function (a, b) {
    return b - a;
  });
  return (array1[1]);
};
console.log(secondBiggest(argv));
