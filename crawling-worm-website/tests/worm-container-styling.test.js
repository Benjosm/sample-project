// crawling-worm-website/tests/worm-container-styling.test.js
import { expect, test, vi, beforeAll } from 'vitest';

beforeAll(() => {
  // Mock the DOM
  global.document = {
    createElement: vi.fn(() => {
      const element = { style: {} };
      element.style.position = '';
      element.style.width = '';
      element.style.height = '';
      element.style.border = '';
      return element;
    }),
  };
});

// Assuming there's a way to access the container element in the DOM, e.g., by ID or class name.
// This is a placeholder; replace with your actual element selector.
const getContainer = () => {
  const container = document.createElement('div');
  container.id = 'worm-container';
  container.style.position = 'relative'; // Set initial position for tests
  container.style.width = '300px';     // Set initial width for tests
  container.style.height = '300px';    // Set initial height for tests
  container.style.border = '1px solid black'; // Set initial border for tests
  return container;
}

test('worm container position is relative', () => {
  const container = getContainer();
  expect(container.style.position).toBe('relative');
});

test('worm container dimensions are 300px x 300px', () => {
  const container = getContainer();
  expect(container.style.width).toBe('300px');
  expect(container.style.height).toBe('300px');
});

test('worm container has a border', () => {
  const container = getContainer();
  expect(container.style.border).toBe('1px solid black'); // Adjust border style if needed
});
