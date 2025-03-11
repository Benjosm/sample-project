// script.js

let direction = 'right'; // Initial direction
const worm = {
  x: 0,
  y: 0
};

const gridSize = 20;
const gameBoardSize = 400; // Example game board size

function changeDirection() {
    const directions = ['up', 'down', 'left', 'right'];
    const newDirection = directions[Math.floor(Math.random() * directions.length)];
    direction = newDirection;
}

function init() {
    setInterval(changeDirection, 1000); // Change direction every 1 second
}

// Function to update worm's position based on direction
function updateWormPosition() {
  switch (direction) {
    case 'up':
      worm.y -= gridSize;
      break;
    case 'down':
      worm.y += gridSize;
      break;
    case 'left':
      worm.x -= gridSize;
      break;
    case 'right':
      worm.x += gridSize;
      break;
  }

  // Boundary checks (Example - implement your game's boundaries)
    if (worm.x < 0) worm.x = 0;
    if (worm.x >= gameBoardSize) worm.x = gameBoardSize - gridSize;
    if (worm.y < 0) worm.y = 0;
    if (worm.y >= gameBoardSize) worm.y = gameBoardSize - gridSize;
}

module.exports = {
    changeDirection, 
    init, 
    updateWormPosition,
    worm
};
