document.addEventListener('DOMContentLoaded', () => {
  const subQuadrants = document.querySelectorAll('.sub-quadrant');

  const colorSetA = {
    quadrant1: {
      subQuadrant1: '#CCCCCC',
      subQuadrant2: '#CCCCCC',
      subQuadrant3: '#CCCCCC',
      subQuadrant4: '#CCCCCC'
    },
    quadrant2: {
      subQuadrant1: '#CCCCCC',
      subQuadrant2: '#CCCCCC',
      subQuadrant3: '#CCCCCC',
      subQuadrant4: '#CCCCCC'
    },
    quadrant3: {
      subQuadrant1: '#CCCCCC',
      subQuadrant2: '#CCCCCC',
      subQuadrant3: '#CCCCCC',
      subQuadrant4: '#CCCCCC'
    },
    quadrant4: {
      subQuadrant1: '#CCCCCC',
      subQuadrant2: '#CCCCCC',
      subQuadrant3: '#CCCCCC',
      subQuadrant4: '#CCCCCC'
    }
  };

  const colorSetB = {
    quadrant1: {
      subQuadrant1: '#000000',
      subQuadrant2: '#FFFFFF',
      subQuadrant3: '#FF00FF',
      subQuadrant4: '#FFFF00'
    },
    quadrant2: {
      subQuadrant1: '#FF0000',
      subQuadrant2: '#00FF00',
      subQuadrant3: '#0000FF',
      subQuadrant4: '#FFA500'
    },
    quadrant3: {
      subQuadrant1: '#800080',
      subQuadrant2: '#008000',
      subQuadrant3: '#FFC0CB',
      subQuadrant4: '#FF4500'
    },
    quadrant4: {
      subQuadrant1: '#808080',
      subQuadrant2: '#FFD700',
      subQuadrant3: '#000080',
      subQuadrant4: '#008080'
    }
  };

  let currentColorSet = 'A';

  Object.keys(colorSetA).forEach((quadrant) => {
    Object.keys(colorSetA[quadrant]).forEach((subQuadrant) => {
      const index = getSubQuadrantIndex(quadrant, subQuadrant);
      const colorA = colorSetA[quadrant][subQuadrant];
      const colorB = colorSetB[quadrant][subQuadrant];

      subQuadrants[index].style.backgroundColor = colorA;

      subQuadrants[index].addEventListener('click', () => {
        if (currentColorSet === 'A') {
          subQuadrants[index].style.backgroundColor = colorB;
          currentColorSet = 'B';
        } else {
          subQuadrants[index].style.backgroundColor = colorA;
          currentColorSet = 'A';
        }
      });
    });
  });

  function getSubQuadrantIndex(quadrant, subQuadrant) {
    const quadrantIndex = parseInt(quadrant.substr(-1)) - 1;
    const subQuadrantIndex = parseInt(subQuadrant.substr(-1)) - 1;
    return quadrantIndex * 4 + subQuadrantIndex;
  }
});
