// Select the element with id 'add_item'
const addItemDiv = document.getElementById('add_item');

// Select the ul element with class 'my_list'
const ul = document.querySelector('.my_list');

// Add a click event listener to the 'add_item' div
addItemDiv.addEventListener('click', function() {
  // Create a new li element
  const li = document.createElement('li');
  
  // Set its content
  li.textContent = 'Item';
  
  // Append the new li to the ul
  ul.appendChild(li);
});
