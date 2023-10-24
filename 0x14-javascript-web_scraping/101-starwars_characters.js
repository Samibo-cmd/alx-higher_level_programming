#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (err) {
  console.log(err);
}

function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let p = 0; p < characters.length; ++p) {
        promises.push(getDataFrom(characters[p]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let p = 0; p < results.length; ++p) {
            console.log(JSON.parse(results[p]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}
printMovieCharacters(process.argv[2]);
