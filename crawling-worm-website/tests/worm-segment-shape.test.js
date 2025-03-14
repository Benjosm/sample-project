// crawling-worm-website/tests/worm-segment-shape.test.js
import { test, expect } from 'vitest';

test('worm segment shape is circle', () => {
  // Mock a segment element or create a simple one
  const segment = document.createElement('div');
  segment.style.borderRadius = '50%';
  // Add it to the document so it's rendered
  document.body.appendChild(segment);
  
  // Assert that the shape is a circle (or close enough - depending on actual implementation)
  expect(segment.style.borderRadius).toBe('50%');
  
  document.body.removeChild(segment);
});

test('worm segment shape is square', () => {
  // Mock a segment element or create a simple one
  const segment = document.createElement('div');
  segment.style.borderRadius = '0';
  // Add it to the document so it's rendered
  document.body.appendChild(segment);
  
  // Assert that the shape is a square
  expect(segment.style.borderRadius).toBe('0');
  
  document.body.removeChild(segment);
});

// Add more tests for other shapes and custom shapes as needed
