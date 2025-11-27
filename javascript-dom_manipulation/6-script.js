// Select the element where the character name will be displayed
const characterDiv = document.getElementById('character');

// Fetch data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    // Update the content of the div with the character name
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
