// Select the header element
const header = document.querySelector('header');

// Select the element with id 'red_header'
const redHeaderDiv = document.getElementById('red_header');

// Add a click event listener to the 'red_header' div
redHeaderDiv.addEventListener('click', function() {
  header.style.color = '#FF0000';
});
