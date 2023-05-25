#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character = JSON.parse(body);
    const innerChar = character.characters;
    for (const i of innerChar) {
      request.get(i, function (error, res, body1) {
        if (error) {
          console.log(error);
        }
        const data1 = JSON.parse(body1);
        console.log(data1.name);
      });
    }
  }
});
