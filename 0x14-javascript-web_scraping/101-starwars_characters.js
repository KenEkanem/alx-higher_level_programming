#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character = JSON.parse(body).characters;
    printCharacters(character, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
