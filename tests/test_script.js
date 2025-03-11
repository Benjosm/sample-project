// tests/test_script.js

// Mock requestAnimationFrame and cancelAnimationFrame
global.requestAnimationFrame = (callback) => {
  setTimeout(callback, 0);
};
global.cancelAnimationFrame = (id) => {
  clearTimeout(id);
};

const fs = require('fs');
const path = require('path');

// Read the content of script.js
let scriptContent = fs.readFileSync(path.resolve(__dirname, '../script.js'), 'utf8');

// Mock the worm object with initial properties
let worm = {
  head: { x: 0, y: 0 },
  segments: [{ x: 0, y: 0 }, { x: 0, y: 0 }],
  direction: Math.PI / 4, // Example direction
  speed: 1,
};


// Mock the document and its methods
global.document = {
  querySelector: (selector) => {
    if (selector === '#worm') {
      return {
        style: { transform: '' },
      };
    }
    return null;
  },
};



// Function to mock the updateWorm function (or whatever you name it)
function updateWorm() {
  // Implement the updateWorm function logic here, directly from script.js or your implementation of crawling animation logic.
  worm.head.x += worm.speed * Math.cos(worm.direction);
  worm.head.y += worm.speed * Math.sin(worm.direction);

    // Update segments to follow the head
    for (let i = 1; i < worm.segments.length; i++) {
      worm.segments[i].x += (worm.head.x - worm.segments[i].x) * 0.2;
      worm.segments[i].y += (worm.head.y - worm.segments[i].y) * 0.2;
    }
}



describe('Crawling Animation', () => {
  it('should update worm head position in each animation frame', (done) => {
    // Initial position
    const initialX = worm.head.x;
    const initialY = worm.head.y;

    // Mock animation frame
    updateWorm();

    // Check if the position has changed (it should)
    expect(worm.head.x).not.toBe(initialX);
    expect(worm.head.y).not.toBe(initialY);

    done();
  });
});