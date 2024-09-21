#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function charac () {
  await request(url, async function req (error, response, body) {
    if (error) {
      console.error('There is an error');
    }
    const characters = await JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      await request(characters[i], async function name (error, response, body) {
        if (error) {
          console.error('Error');
        }
        const character = await JSON.parse(body).name;
        await console.log(character);
      });
    }
  });
}

charac();
