// crawling-worm-website/script.js

import { gsap } from "gsap";

// Define the worm object (assuming this is already defined)
let worm = {
    x: 50, // Initial X position
    y: 50, // Initial Y position
    direction: 'right', // Initial direction
    speed: 150, // Movement speed (pixels per second)
    segmentSize: 10, // Size of each segment
    segments: [] // Array to store the segments of the worm's body
};

// Define the canvas and context (assuming this is already defined)
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Function to update the worm's position and direction using GSAP
function update() {
    let targetX = worm.x;
    let targetY = worm.y;

    // Determine target coordinates based on direction
    switch (worm.direction) {
        case 'up':
            targetY -= worm.segmentSize; // Move segmentSize pixels in the y-direction
            break;
        case 'down':
            targetY += worm.segmentSize; // Move segmentSize pixels in the y-direction
            break;
        case 'left':
            targetX -= worm.segmentSize; // Move segmentSize pixels in the x-direction
            break;
        case 'right':
            targetX += worm.segmentSize; // Move segmentSize pixels in the x-direction
            break;
    }

    // Calculate duration based on speed
    const duration = worm.segmentSize / worm.speed; // Duration is proportional to distance and inversely proportional to speed

    // Animate the movement using GSAP
    gsap.to(worm, {
        x: targetX,
        y: targetY,
        duration: duration,
        ease: "power1.inOut", // Experiment with different easing functions
        onComplete: () => {
            // Add the current head position to the segments array after movement
            worm.segments.unshift({ x: worm.x, y: worm.y });

            // Limit the worm's body length to a certain number of segments
            if (worm.segments.length > 10) {
              worm.segments.pop(); // Remove the tail
            }
            // Check for collision with the canvas boundaries after movement
            checkBoundaryCollisions();
        }
    });

    // Implement random direction change after movement
    if (Math.random() < 0.05) { // Adjust the probability for desired frequency
        const directions = ['up', 'down', 'left', 'right'];
        worm.direction = directions[Math.floor(Math.random() * directions.length)];
    }
}

function checkBoundaryCollisions() {
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

// Function to draw the worm
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'green';

    // Draw the worm's head
    ctx.fillRect(worm.x, worm.y, worm.segmentSize, worm.segmentSize);

    // Draw the worm's segments (body)
    ctx.fillStyle = 'lightgreen';
    for (let i = 0; i < worm.segments.length; i++) {
        ctx.fillRect(worm.segments[i].x, worm.segments[i].y, worm.segmentSize, worm.segmentSize);
    }
}

// Use GSAP.ticker for the animation loop
gsap.ticker.add(() => {
    update();
    draw();
});