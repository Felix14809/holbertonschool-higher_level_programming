const movies = document.querySelector('#list_movies');
const header = document.querySelector('header');
header.addEventListener('click', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => response.json())
    .then((data) => {
      data.results.forEach((movie) => {
        const movieTitle = document.createElement('li');
        movieTitle.textContent = movie.title;
        movies.appendChild(movieTitle);
      });
    });
}, { once: true });

header.addEventListener('mouseover', () => {
  header.style.cursor = 'pointer';
});

header.addEventListener('mouseout', () => {
  header.style.cursor = 'default';
});
