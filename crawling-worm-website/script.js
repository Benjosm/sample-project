// crawling-worm-website/script.js

// Define the worm object (assuming this is already defined)
let worm = {
    x: 50, // Initial X position
    y: 50, // Initial Y position
    direction: 'right', // Initial direction
    speed: 2, // Movement speed
    segments: [] // Array to store the segments of the worm's body
};

// Define the canvas and context (assuming this is already defined)
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Function to update the worm's position and direction
function update() {
    // Move the worm based on its current direction
    switch (worm.direction) {
        case 'up':
            worm.y -= worm.speed;
            break;
        case 'down':
            worm.y += worm.speed;
            break;
        case 'left':
            worm.x -= worm.speed;
            break;
        case 'right':
            worm.x += worm.speed;
            break;
    }

    // Implement random direction change
    if (Math.random() < 0.02) { // Adjust the probability for desired frequency
        const directions = ['up', 'down', 'left', 'right'];
        worm.direction = directions[Math.floor(Math.random() * directions.length)];
    }

    // Add the current head position to the segments array
    worm.segments.unshift({ x: worm.x, y: worm.y });

    // Limit the worm's body length to a certain number of segments
    if (worm.segments.length > 10) {
      worm.segments.pop(); // Remove the tail
    }


    // Check for collision with the canvas boundaries
    if (worm.x < 0) {
        worm.x = 0;
        worm.direction = 'right';
    }
    if (worm.x > canvas.width) {
        worm.x = canvas.width;
        worm.direction = 'left';
    }
    if (worm.y < 0) {
        worm.y = 0;
        worm.direction = 'down';
    }
    if (worm.y > canvas.height) {
        worm.y = canvas.height;
        worm.direction = 'up';
    }
}

// Function to draw the worm
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'green';

    // Draw the worm's head
    ctx.fillRect(worm.x, worm.y, 10, 10);

    // Draw the worm's segments (body)
    for (let i = 0; i < worm.segments.length; i++) {
        ctx.fillRect(worm.segments[i].x, worm.segments[i].y, 10, 10);
    }
}

// Game loop
function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();