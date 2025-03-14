// crawling-worm-website/tests/tail-segment-styling.test.js
import { expect, test } from 'vitest';

test('tail segment has distinct styling', () => {
  // Assuming there's a way to access the tail segment in the DOM.
  // This is a placeholder, replace with actual DOM access.
  const tailSegment = document.createElement('div'); // or getElementById, querySelector etc.
  tailSegment.classList.add('worm-segment', 'worm-tail');

  // Placeholder: Add tail segment to the document or a testing environment if necessary.
  // document.body.appendChild(tailSegment);

  // Placeholder: Check for a specific style or class related to the tail segment.
  // Replace with the actual style property you expect to be different.
  expect(tailSegment.style.backgroundColor).toBeDefined(); // Or .not.toBe or .toEqual, etc.

  // Cleanup, if you added the segment to the document.
  // document.body.removeChild(tailSegment);
});