#!/usr/bin/node

const req = require('request'); // using req as the alias for request
const movieId = process.argv[2];
const urlApi = `https://swapi-api.hbtn.io/api/films/${movieId}`;

req(urlApi, async (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const charactersArray = JSON.parse(body).characters;
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      req(character, (err, res, body) => {
        if (err) {
          console.log(err);
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
