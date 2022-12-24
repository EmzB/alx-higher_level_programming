#!/usr/bin/node
/**
  get the title of a Star Wars movie 
  match the episode number with the given Integer
 */
const myArgs = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request(url, function (error, response, body) {
  if (!error) {
    const json_ = JSON.parse(body);
    console.log(json_.title);
  }
});
