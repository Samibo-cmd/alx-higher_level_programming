#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let p = 0; p < body.length; ++p) {
    const characters = body[p].characters;

    for (let q = 0; q < characters.length; ++q) {
      const character = characters[q];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});
