#!/usr/bin/node

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);

async function fetchFilmCharacters (filmId) {
  const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

  try {
    const filmResponse = await requestPromise(url);
    const filmData = JSON.parse(filmResponse.body);

    const characterPromises = filmData.characters.map(async (characterUrl) => {
      const characterResponse = await requestPromise(characterUrl);
      return JSON.parse(characterResponse.body).name;
    });

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(`Failed to fetch data: ${error.message}`);
  }
}

const filmId = process.argv[2];
fetchFilmCharacters(filmId);
