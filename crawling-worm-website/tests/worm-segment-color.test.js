// crawling-worm-website/tests/worm-segment-color.test.js
import { test, expect } from 'vitest';

// Assuming you have a function or mechanism to create a worm segment element.
// This is a placeholder, replace it with your actual implementation.
function createSegment(color) {
  const segment = document.createElement('div');
  segment.style.backgroundColor = color;
  return segment;
}

test('worm segment color should be red', () => {
  const segment = createSegment('red');
  expect(segment.style.backgroundColor).toBe('red');
});

test('worm segment color should be blue', () => {
  const segment = createSegment('blue');
  expect(segment.style.backgroundColor).toBe('blue');
});

test('worm segment color should be green', () => {
  const segment = createSegment('green');
  expect(segment.style.backgroundColor).toBe('green');
});
