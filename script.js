// script.js

// Get the viewport dimensions.
const viewportWidth = window.innerWidth;
const viewportHeight = window.innerHeight;

// Define the worm's initial position and direction.
let wormX = 50; // Initial X coordinate (percentage)
let wormY = 50; // Initial Y coordinate (percentage)
let wormDirectionX = 1; // 1 or -1
let wormDirectionY = 1; // 1 or -1
let wormSpeed = 2; //worm speed

// Function to update worm position.
function updateWormPosition() {
    // Calculate the worm's new position.
    let newX = wormX + wormDirectionX * wormSpeed;
    let newY = wormY + wormDirectionY * wormSpeed;

    // Boundary Collision Detection
    if (newX < 0 || newX > 100) {
        // Reverse direction if hit left or right boundary
        wormDirectionX *= -1;
    }
    if (newY < 0 || newY > 100) {
        // Reverse direction if hit top or bottom boundary
        wormDirectionY *= -1;
    }

    // Update worm position
    wormX = wormX + wormDirectionX * wormSpeed;
    wormY = wormY + wormDirectionY * wormSpeed;
    // Apply changes to worm position
    updateWormDisplay();
}

function updateWormDisplay() {
    const worm = document.getElementById('worm');
    if (worm) {
      worm.style.left = wormX + '%';
      worm.style.top = wormY + '%';
    }
}

// Main game loop
function gameLoop() {
    updateWormPosition();
    // Redraw the worm or update its position visually
    // Repeat the function
    requestAnimationFrame(gameLoop);
}

// Start the game loop when the page loads.
window.onload = () => {
    // Create the worm element
    const worm = document.createElement('div');
    worm.id = 'worm';
    worm.style.position = 'absolute';
    worm.style.width = '20px'; // Adjust as needed
    worm.style.height = '20px'; // Adjust as needed
    worm.style.backgroundColor = 'green'; // Or any other color
    worm.style.left = wormX + '%';
    worm.style.top = wormY + '%';
    document.body.appendChild(worm);
    gameLoop();
};
