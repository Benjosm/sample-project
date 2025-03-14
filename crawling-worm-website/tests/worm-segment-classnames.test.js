// crawling-worm-website/tests/worm-segment-classnames.test.js
import { describe, it, expect } from 'vitest';

// Assuming you have a way to generate or access the worm segments HTML
const getWormSegments = () => {
  // This is placeholder. Replace with actual logic to generate HTML elements.
  // For example, you might parse HTML from a string or access elements in the DOM.
  return [
    { outerHTML: '<div class="segment"></div>' },
    { outerHTML: '<div class="segment"></div>' },
    { outerHTML: '<div class="segment"></div>' },
  ];
};

describe('Worm Segment Class Names', () => {
  it('should have the correct class name (worm-segment)', () => {
    const segments = getWormSegments();
    segments.forEach(segment => {
      expect(segment.outerHTML).toContain('class="worm-segment"');
    });
  });
});