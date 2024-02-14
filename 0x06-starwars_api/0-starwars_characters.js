#!/usr/bin/node
// Print all characters of a Star Wars movie

const request = require('request');

if (process.argv.length < 3) {
  console.error(`Usage: node 0-starwars_character.js <id>`);
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

    characters.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
	if (error) console.error(`Error fetching data: ${error}`);
	else if (response.statusCode !== 200) {
	  console.error(`Status ${response.statusCode} fetching data`);
	} else {
	  const character = JSON.parse(body);
	  console.log(`${character.name}`);
	}
      });
    });
  }
});
