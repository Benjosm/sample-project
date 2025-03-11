// tests/test_script.js

const { JSDOM } = require('jsdom');

// Mock the document and window objects
const dom = new JSDOM('<!DOCTYPE html><html><head></head><body><div id="worm"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;

require('../script.js');

describe('Boundary Collision Detection', () => {
  beforeEach(() => {
    // Reset worm position and direction before each test
    window.wormX = 50;
    window.wormY = 50;
    window.wormDirectionX = 1;
    window.wormDirectionY = 1;
    document.body.innerHTML = '<div id="worm"></div>'; // Reset worm element
  });

  it('should reverse direction when hitting left boundary', () => {
    window.wormX = -1; // Simulate hitting left boundary
    updateWormPosition();
    expect(window.wormDirectionX).toBe(-1); // Should now be moving right
  });

  it('should reverse direction when hitting right boundary', () => {
    window.wormX = 101; // Simulate hitting right boundary
    updateWormPosition();
    expect(window.wormDirectionX).toBe(-1); // Should now be moving left
  });

  it('should reverse direction when hitting top boundary', () => {
    window.wormY = -1; // Simulate hitting top boundary
    updateWormPosition();
    expect(window.wormDirectionY).toBe(-1); // Should now be moving down
  });

  it('should reverse direction when hitting bottom boundary', () => {
    window.wormY = 101; // Simulate hitting bottom boundary
    updateWormPosition();
    expect(window.wormDirectionY).toBe(-1); // Should now be moving up
  });
});