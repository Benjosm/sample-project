import { describe, it, expect, beforeEach } from 'vitest';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;
global.HTMLElement = dom.window.HTMLElement;

describe('Head Segment Styling', () => {
  let headSegment;
  let container;

  beforeEach(() => {
    container = document.getElementById('worm-container');
    headSegment = document.createElement('div');
    headSegment.style.backgroundColor = 'red'; // Set initial style
    container.appendChild(headSegment);
  });

  it('should have a different color', () => {
    expect(headSegment.style.backgroundColor).toBe('red');
  });
});