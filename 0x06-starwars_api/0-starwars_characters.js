#!/usr/bin/node
// Fetching star wars characters from an api
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(`Status ${response.statusCode}`);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Function to fetch and print character data
    const printCharacterData = (characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error fetching character data: ${error}`);
        } else if (response.statusCode !== 200) {
          console.error(`Status ${response.statusCode} fetching character data`);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };

    // Loop through each character URL and print character name
    characters.forEach(printCharacterData);
  }
});
