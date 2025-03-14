// crawling-worm-website/tests/worm-segment-count.test.js
import { describe, it, expect, beforeEach } from 'vitest';

// Mock the DOM for testing
const mockHTML = `
  <div class="worm-segment"></div>
  <div class="worm-segment"></div>
  <div class="worm-segment"></div>
`;

beforeEach(() => {
  document.body.innerHTML = mockHTML;
});

describe('Worm Segment Count', () => {
  it('should have the correct number of worm segments', () => {
    const wormSegments = document.querySelectorAll('.worm-segment');
    expect(wormSegments.length).toBe(3);
  });
});
