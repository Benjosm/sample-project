// crawling-worm-website/tests/worm-segment-size.test.js
import { expect, test } from 'vitest';

// Mock a simple worm segment element for testing.
const createSegment = (width, height) => {
  const segment = document.createElement('div');
  segment.style.width = `${width}px`;
  segment.style.height = `${height}px`;
  segment.classList.add('worm-segment'); // Assuming this class is used for styling.
  return segment;
};

// Mock the document since we are running in a Node.js environment
global.document = {
  createElement: (tagName) => {
    if (tagName === 'div') {
      return {style: { width: '', height: '' }, classList: { add: (className) => {}}};
    }
  }
};

test('worm segment size should match specified dimensions', () => {
  const width = 20;
  const height = 10;
  const segment = createSegment(width, height);

  expect(segment.style.width).toBe(`${width}px`);
  expect(segment.style.height).toBe(`${height}px`);
});

test('worm segment size with different dimensions', () => {
  const width = 30;
  const height = 15;
  const segment = createSegment(width, height);

  expect(segment.style.width).toBe(`${width}px`);
  expect(segment.style.height).toBe(`${height}px`);
});
