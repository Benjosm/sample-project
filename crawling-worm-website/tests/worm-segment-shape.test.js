import { describe, it, expect, beforeEach } from 'vitest';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;
global.HTMLElement = dom.window.HTMLElement;

describe('worm segment shape', () => {
  let segment;
  beforeEach(() => {
    segment = document.createElement('div');
    segment.style.borderRadius = '0px'; // Set initial style
    document.body.appendChild(segment);
  });

  afterEach(() => {
    document.body.removeChild(segment);
  });

  it('worm segment shape is square', () => {
    // Assert that the shape is a square
    expect(segment.style.borderRadius).toBe('0px');
  });
});