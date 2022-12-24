#!/usr/bin/node
/**
  display the return status of a GET request
  pass URL as argument
  */
const myArgs = process.argv.slice(2);
const request = require('request');
request(myArgs[0], function (error, response, body) {
  if (!error && response) {
    console.log('code:', response.statusCode);
  }
});
