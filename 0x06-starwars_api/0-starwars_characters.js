#!/usr/bin/node
// Fetching star wars characters from an api

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch character data
const fetchCharacterData = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(`Error fetching character data: ${error}`);
      } else if (response.statusCode !== 200) {
        reject(`Status ${response.statusCode} fetching character data`);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Status ${response.statusCode}`);
    process.exit(1);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Fetch character data for each character URL asynchronously
    Promise.all(characters.map(fetchCharacterData))
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
        process.exit(1);
      });
  }
});
