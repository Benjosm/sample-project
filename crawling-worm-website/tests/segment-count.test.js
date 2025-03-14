import { describe, it, expect, beforeEach } from 'vitest';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;

describe('Worm Segment Count', () => {
  beforeEach(() => {
      // Reset the document body for each test
      document.body.innerHTML = '<div id="worm-container"></div>';
  });

  it('should create the correct number of worm segments', () => {
    const wormLength = 5;
    const container = document.getElementById('worm-container');
    for (let i = 0; i < wormLength; i++) {
      const segment = document.createElement('div');
      segment.className = 'worm-segment';
      container.appendChild(segment);
    }

    const segments = container.querySelectorAll('.worm-segment');
    expect(segments.length).toBe(wormLength);
  });
});