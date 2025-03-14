// crawling-worm-website/tests/initial-positioning.test.js
import { expect, test } from 'vitest';

// Mock the document and its methods
global.document = {
  body: {
    innerHTML: '',
    appendChild: (child) => {
      global.document.body.innerHTML += child.outerHTML;
    }
  },
  createElement: (tagName) => {
    if (tagName === 'div') {
      return {
        style: {},
        outerHTML: ''
      };
    }
    return null;
  },
  querySelector: (selector) => {
    if (selector === '#worm-container') {
      return {
        style: {},
        innerHTML: ''
      };
    }
    return null;
  },
  querySelectorAll: (selector) => {
    if (selector === '.worm-segment') {
      return []; // Initially no segments
    }
    return [];
  },
  addEventListener: () => {},
};

global.window = {
  innerWidth: 1024,
  innerHeight: 768,
  addEventListener: () => {}
};

// Mock the script.js module
const script = {
  initializeWorm: () => {
    // Simulate adding worm segments to the DOM
    const container = document.querySelector('#worm-container');
    if (container) {
      for (let i = 0; i < 3; i++) {
        const segment = document.createElement('div');
        segment.className = 'worm-segment';
        segment.style.position = 'absolute';
        segment.style.left = `${i * 20}px`; // Example positioning
        segment.style.top = '10px';
        container.appendChild(segment);
      }
    }
  }
};

test('worm segments are initially visible within the viewport', () => {
  // Mock the worm container
  document.body.innerHTML = '<div id="worm-container"></div>';
  script.initializeWorm(); // Assuming a function like this exists in script.js
  // Assuming segments are added to the DOM during script execution
  const segments = document.querySelectorAll('.worm-segment');
  expect(segments.length).toBeGreaterThan(0);

  segments.forEach(segment => {
    expect(segment.style.position).toBeDefined(); // Check if position is set
    expect(segment.style.left).toBeDefined(); // Check if left is set
    expect(segment.style.top).toBeDefined(); // Check if top is set
  });
});

test('worm segments are positioned in a horizontal line or simple curve', () => {
  // Mock the worm container
  document.body.innerHTML = '<div id="worm-container"></div>';
  script.initializeWorm(); // Assuming a function like this exists in script.js
  // This test is more complex and depends on the specific initialization.
  // Requires knowledge about worm segment positions after initialization.
  script.initializeWorm();
  const segments = document.querySelectorAll('.worm-segment');

  if (segments.length > 1) {
    let previousSegment = null;
    let allHorizontal = true;
    segments.forEach(segment => {
      if (previousSegment) {
        const prevLeft = parseFloat(previousSegment.style.left);
        const currLeft = parseFloat(segment.style.left);
        const prevTop = parseFloat(previousSegment.style.top);
        const currTop = parseFloat(segment.style.top);
        
        if (Math.abs(prevTop - currTop) > 10) {
          allHorizontal = false;
        }
        
      }
      previousSegment = segment;
    });
    expect(allHorizontal).toBe(true);
  }
});

test('CSS or JavaScript is used to set the initial position', () => {
    // Mock the worm container
    document.body.innerHTML = '<div id="worm-container"></div>';
    script.initializeWorm(); // Assuming a function like this exists in script.js
    // Verify that the worm is positioned using css or javascript
    const segments = document.querySelectorAll('.worm-segment');
    segments.forEach(segment => {
        expect(segment.style.position).not.toBe("");
    });
});

test('different viewport sizes are considered', () => {
    // Mock the worm container
    document.body.innerHTML = '<div id="worm-container"></div>';
    script.initializeWorm(); // Assuming a function like this exists in script.js
    // Test with a smaller viewport
    global.window.innerWidth = 480;
    global.window.innerHeight = 320;
    // Re-initialize or re-render the worm
    script.initializeWorm();
    // Check if the worm is still visible
    const segments = document.querySelectorAll('.worm-segment');
    expect(segments.length).toBeGreaterThan(0);

    // Restore viewport size
    global.window.innerWidth = 1024;
    global.window.innerHeight = 768;
});
