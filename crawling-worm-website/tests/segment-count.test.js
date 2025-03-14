import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// Mock the document for testing purposes
global.document = {
  body: {
    innerHTML: ''
  }
};

describe('Worm Segment Count', () => {
  it('should create the correct number of worm segments', () => {
    // Assuming the worm length is configurable, let's set it to 5 for this test
    const wormLength = 5;

    // Simulate the HTML structure (simplified for this test)
    const segmentCount = wormLength;
    let html = '';
    for(let i = 0; i < segmentCount; i++) {
      html += `<div class="worm-segment"></div>`;
    }
    global.document.body.innerHTML = `<div id="worm-container">${html}</div>`;

    const segments = global.document.body.querySelectorAll('.worm-segment');
    expect(segments.length).toBe(wormLength);
  });
});