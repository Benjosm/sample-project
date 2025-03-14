// crawling-worm-website/script.js

// Import GSAP
import { gsap } from "gsap";

// --- Configuration --- 

// Define the worm object
let worm = {
    x: 50, // Initial X position (pixels)
    y: 50, // Initial Y position (pixels)
    direction: 'right', // Initial direction (up, down, left, right)
    speed: 150, // Movement speed (pixels per second)
    segmentSize: 10, // Size of each segment (pixels)
    segments: [] // Array to store the segments of the worm's body
};

// --- Setup --- 

// Get the canvas element and its 2D rendering context
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Ensure the canvas is available before proceeding.  This prevents errors if the script loads before the canvas element.
if (!canvas || !ctx) {
  console.error("Canvas element or context not found.  Ensure the canvas element with id 'gameCanvas' exists in your HTML.");
}

// --- Core Functions --- 

/**
 * Updates the worm's position and direction using GSAP for smooth animation.
 */
function update() {
    // Calculate target coordinates based on the current direction.
    let targetX = worm.x;
    let targetY = worm.y;

    switch (worm.direction) {
        case 'up':
            targetY -= worm.segmentSize;
            break;
        case 'down':
            targetY += worm.segmentSize;
            break;
        case 'left':
            targetX -= worm.segmentSize;
            break;
        case 'right':
            targetX += worm.segmentSize;
            break;
    }

    // Calculate animation duration based on the worm's speed and segment size.
    const duration = worm.segmentSize / worm.speed; // Duration is proportional to distance and inversely proportional to speed

    // Use GSAP to animate the worm's movement.
    gsap.to(worm, {
        x: targetX,
        y: targetY,
        duration: duration,
        ease: "linear", // Linear ease for consistent speed.
        onComplete: () => {
            // Add the current head position as a new segment after movement.
            worm.segments.unshift({ x: worm.x, y: worm.y });

            // Limit the worm's body length to prevent it from growing indefinitely.
            if (worm.segments.length > 10) {
              worm.segments.pop(); // Remove the tail segment
            }
            // Check for and handle boundary collisions.
            checkBoundaryCollisions();
        }
    });

    // Randomly change the worm's direction.
    if (Math.random() < 0.05) { // 5% chance of changing direction
        const directions = ['up', 'down', 'left', 'right'];
        worm.direction = directions[Math.floor(Math.random() * directions.length)];
    }
}

/**
 * Checks for collisions with the canvas boundaries and adjusts the worm's direction accordingly.
 */
function checkBoundaryCollisions() {
    // Prevent the worm from going out of bounds.
    if (worm.x < 0) {
        worm.x = 0;
        worm.direction = 'right';
    }
    if (worm.x > canvas.width - worm.segmentSize) {
        worm.x = canvas.width - worm.segmentSize;
        worm.direction = 'left';
    }
    if (worm.y < 0) {
        worm.y = 0;
        worm.direction = 'down';
    }
    if (worm.y > canvas.height - worm.segmentSize) {
        worm.y = canvas.height - worm.segmentSize;
        worm.direction = 'up';
    }
}

/**
 * Draws the worm on the canvas.
 */
function draw() {
    // Clear the canvas before each frame.
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the worm's head.
    ctx.fillStyle = 'green';
    ctx.fillRect(worm.x, worm.y, worm.segmentSize, worm.segmentSize);

    // Draw the worm's segments (body).
    ctx.fillStyle = 'lightgreen';
    for (let i = 0; i < worm.segments.length; i++) {
        ctx.fillRect(worm.segments[i].x, worm.segments[i].y, worm.segmentSize, worm.segmentSize);
    }
}

// --- Animation Loop --- 

// Use GSAP's ticker for the animation loop, ensuring smooth and efficient updates.
gsap.ticker.add(() => {
    if (canvas && ctx) { // Only run if canvas and context exist
        update();
        draw();
    }
});
