#!/usr/bin/node

const request = require('request');
/**
 * The URL for the Star Wars API endpoint.
 * @type {string}
 */
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const character of data.characters) {
      request(character, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    }
  }
});
