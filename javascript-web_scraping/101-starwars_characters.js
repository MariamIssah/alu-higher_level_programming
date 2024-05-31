#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  console.log('Characters in', movie.title + ':');

  const characterPromises = movie.characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(`Failed to fetch character data. Status code: ${response.statusCode}`);
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error(error);
    });
});
