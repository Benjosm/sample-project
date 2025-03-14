// JavaScript for animations and logic

document.addEventListener('DOMContentLoaded', () => {
  const wormSegments = document.querySelectorAll('.worm-segment');
  const segmentSpacing = 20; // Space between segments
  const startX = 50; // Starting X position
  const startY = 50; // Starting Y position

  wormSegments.forEach((segment, index) => {
    segment.style.position = 'absolute';
    segment.style.left = `${startX + index * segmentSpacing}px`;
    segment.style.top = `${startY}px`;
  });
});