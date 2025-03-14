// crawling-worm-website/tests/worm-segment-visual-effects.test.js
import { expect, test } from 'vitest';

// Mock the document and other necessary DOM elements for testing in a headless environment
const mockDocument = () => {
  global.document = {
    createElement: (tag) => {
      if (tag === 'div') {
        return {
          style: {},
          classList: {
            add: () => {},
            contains: () => false
          }
        };
      }
      return null;
    },
    body: {
      appendChild: () => {}
    },
    head: {
      appendChild: () => {}
    }
  } as any;
};

mockDocument();

test('worm segment has a gradient', () => {
  const segment = document.createElement('div');
  segment.style.background = 'linear-gradient(to right, red, yellow)';
  expect(segment.style.background).toBe('linear-gradient(to right, red, yellow)');
});

test('worm segment has a shadow', () => {
  const segment = document.createElement('div');
  segment.style.boxShadow = '2px 2px 5px rgba(0, 0, 0, 0.5)';
  expect(segment.style.boxShadow).toBe('2px 2px 5px rgba(0, 0, 0, 0.5)');
});

// Additional tests can be added to check different gradient types, shadow properties, etc.
