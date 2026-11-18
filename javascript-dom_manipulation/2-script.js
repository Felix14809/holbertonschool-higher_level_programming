const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', () => {
  document.querySelector('header').classList.add('red');
});
redHeader.addEventListener('mouseover', () => {
  redHeader.style.cursor = 'pointer';
});
redHeader.addEventListener('mouseout', () => {
  redHeader.style.cursor = 'default';
});
