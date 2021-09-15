#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, result, body) => {
  if (err) {
    console.error(err);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, result) { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});
