const header = document.querySelector('header');
header.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
header.addEventListener('mouseover', () => {
  header.style.cursor = 'pointer';
});
header.addEventListener('mouseout', () => {
  header.style.cursor = 'default';
});
