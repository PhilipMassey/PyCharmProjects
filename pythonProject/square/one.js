document.addEventListener('DOMContentLoaded', () => {
  const subQuadrants = document.querySelectorAll('.sub-quadrant');

  subQuadrants.forEach((subQuadrant) => {
    subQuadrant.addEventListener('click', () => {
      subQuadrant.style.backgroundColor = getRandomColor();
    });
  });

  function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';

    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }

    return color;
  }
});
