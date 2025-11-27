// Select the header element
const header = document.querySelector('header');

// Select the element with id 'update_header'
const updateDiv = document.getElementById('update_header');

// Add a click event listener to update the header text
updateDiv.addEventListener('click', function() {
  header.textContent = 'New Header!!!';
});
