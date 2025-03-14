// crawling-worm-website/script.js

// Select all worm segments
const wormSegments = document.querySelectorAll('.worm-segment');

// Function to animate a single segment
function animateSegment(segment, index) {
  gsap.to(segment, {
    x: 200, // Move horizontally to the right
    duration: 1, // Animation duration
    delay: index * 0.2, // Stagger animation with a delay
    ease: "power1.inOut", // Easing function
    onComplete: () => {
      // Reset position after animation
      gsap.set(segment, { x: 0 });
      // Optionally, repeat the animation
      animateSegment(segment, index);
    }
  });
}

// Animate each segment
wormSegments.forEach((segment, index) => {
  animateSegment(segment, index);
});