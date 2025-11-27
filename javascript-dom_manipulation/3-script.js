// Select the header element
const header = document.querySelector('header');

// Select the element with id 'toggle_header'
const toggleDiv = document.getElementById('toggle_header');

// Add a click event listener to toggle the header class
toggleDiv.addEventListener('click', function() {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
