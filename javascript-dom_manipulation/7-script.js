// Select the ul element where movie titles will be listed
const listMovies = document.getElementById('list_movies');

// Fetch data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    // Iterate over each movie in the results
    data.results.forEach(movie => {
      // Create a new li element
      const li = document.createElement('li');
      // Set the text content to the movie title
      li.textContent = movie.title;
      // Append the li to the ul
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
