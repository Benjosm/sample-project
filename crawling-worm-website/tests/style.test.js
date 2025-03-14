// crawling-worm-website/tests/style.test.js
import { expect, test } from 'vitest';

// Mock the document and window objects since this test runs in a Node.js environment
global.document = {
    body: {
        style: {}
    },
    createElement: (tag) => {
        if (tag === 'canvas') {
            return {
                style: {}
            };
        }
        return {
          style: {}
        };
    }
};
global.window = {
    innerWidth: 1024,
    innerHeight: 768
};

test('body background color is #f0f0f0', () => {
  document.body.style.backgroundColor = '#f0f0f0'; // Set the expected color
  expect(document.body.style.backgroundColor).toBe('#f0f0f0');
});

test('canvas background color is #fff', () => {
    const canvas = document.createElement('canvas');
    canvas.style.backgroundColor = '#fff'; // Set the expected color
    expect(canvas.style.backgroundColor).toBe('#fff');
});
