document.addEventListener('DOMContentLoaded', () => {
  const subQuadrants = document.querySelectorAll('.sub-quadrant');

const colorSetA = [
  ['#CCCCCC', '#CCCCCC', '#CCCCCC', '#CCCCCC'],
  ['#CCCCCC', '#CCCCCC', '#CCCCCC', '#CCCCCC'],
  ['#CCCCCC', '#CCCCCC', '#CCCCCC', '#CCCCCC'],
  ['#CCCCCC', '#CCCCCC', '#CCCCCC', '#CCCCCC']
];

const colorSetB = [
  ['#000000', '#FFFFFF', '#FF00FF', '#FFFF00'],
  ['#FF0000', '#00FF00', '#0000FF', '#FFA500'],
  ['#800080', '#008000', '#FFC0CB', '#FF4500'],
  ['#808080', '#FFD700', '#000080', '#008080']
];

  let currentColorSet = 'A';

  subQuadrants.forEach((subQuadrant, index) => {
    subQuadrant.style.backgroundColor = colorSetA[Math.floor(index / 4)][index % 4];

    subQuadrant.addEventListener('click', () => {
      if (currentColorSet === 'A') {
        subQuadrant.style.backgroundColor = colorSetB[Math.floor(index / 4)][index % 4];
        currentColorSet = 'B';
      } else {
        subQuadrant.style.backgroundColor = colorSetA[Math.floor(index / 4)][index % 4];
        currentColorSet = 'A';
      }
    });
  });
});
