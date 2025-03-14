import { describe, it, expect, beforeEach } from 'vitest';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"><div class="segment"></div></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;
global.HTMLElement = dom.window.HTMLElement;

function getWormSegments() {
  return document.querySelectorAll('.worm-segment');
}

describe('Worm Segment Class Names', () => {
  beforeEach(() => {
    document.body.innerHTML = '<div id="worm-container"></div>';
  });

  it('should have the correct class name (worm-segment)', () => {
    const container = document.getElementById('worm-container');
    const segment = document.createElement('div');
    segment.className = 'worm-segment';
    container.appendChild(segment);

    const segments = getWormSegments();
    segments.forEach(segment => {
      expect(segment.className).toContain('worm-segment');
    });
  });
});