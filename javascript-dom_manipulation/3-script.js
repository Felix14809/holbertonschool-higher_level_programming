const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');
toggleHeader.addEventListener('click', () => {
  header.classList.toggle('red');
  header.classList.toggle('green');
});

toggleHeader.addEventListener('mouseover', () => {
  toggleHeader.style.cursor = 'pointer';
});
toggleHeader.addEventListener('mouseout', () => {
  toggleHeader.style.cursor = 'default';
});
