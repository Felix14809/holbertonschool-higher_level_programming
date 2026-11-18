const character = document.querySelector('#character');
const header = document.querySelector('header');
header.addEventListener('click', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => response.json())
    .then((data) => {
      character.textContent = data.name;
    });
});

header.addEventListener('mouseover', () => {
  header.style.cursor = 'pointer';
});

header.addEventListener('mouseout', () => {
  header.style.cursor = 'default';
});
