const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

updateHeader.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});

updateHeader.addEventListener('mouseover', () => {
  updateHeader.style.cursor = 'pointer';
});
updateHeader.addEventListener('mouseout', () => {
  updateHeader.style.cursor = 'default';
});
