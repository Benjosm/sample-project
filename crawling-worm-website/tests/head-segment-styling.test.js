// crawling-worm-website/tests/head-segment-styling.test.js
import { describe, it, expect, beforeEach, afterEach } from 'vitest';

// Mock the DOM environment
beforeEach(() => {
  document.body.innerHTML = ''; // Clear the body before each test
});

afterEach(() => {
  // Clean up after each test
  document.body.innerHTML = '';
});

describe('Head Segment Styling', () => {
  it('should have a different color', () => {
    // Assuming the head segment has a class 'worm-segment-head'
    const headSegment = document.createElement('div');
    headSegment.className = 'worm-segment-head';
    document.body.appendChild(headSegment);
    headSegment.style.backgroundColor = 'red'; // Initially set to red

    expect(headSegment.style.backgroundColor).toBe('blue'); // Expecting blue, so the test should fail
  });
});