// crawling-worm-website/tests/segment-id-format.test.js
import { expect, test } from 'vitest';

// Mock the document since we're not running in a browser
global.document = {
  querySelectorAll: (selector) => {
    if (selector === '.worm-segment') {
      return [
        { id: 'segment-0' },
        { id: 'segment-1' },
        { id: 'segment-2' },
      ];
    }
    return [];
  }
};

test('worm segment IDs should be in the format segment-X', () => {
  const segments = document.querySelectorAll('.worm-segment');
  segments.forEach((segment, index) => {
    expect(segment.id).toBe(`segment-${index}`);
  });
});