const hello = document.querySelector('#hello');

document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      hello.textContent = data.hello;
    });
});
