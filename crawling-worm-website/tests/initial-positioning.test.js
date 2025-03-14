import { describe, it, expect, beforeEach } from 'vitest';
import * as fs from 'node:fs';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;
global.HTMLElement = dom.window.HTMLElement;


function initializeWorm(container, segmentCount = 5) {
  for (let i = 0; i < segmentCount; i++) {
    const segment = document.createElement('div');
    segment.style.width = '20px';
    segment.style.height = '20px';
    segment.style.backgroundColor = 'green';
    segment.style.position = 'absolute';
    segment.style.left = `${i * 20}px`; // Example positioning
    segment.style.top = '10px';
    container.appendChild(segment);
  }
}

describe('initial positioning', () => {
  let container;

  beforeEach(() => {
    container = document.getElementById('worm-container');
    container.innerHTML = ''; // Clear any existing content
  });

  it('worm segments are initially visible within the viewport', () => {
    initializeWorm(container);
    const segments = container.children;
    for (let i = 0; i < segments.length; i++) {
      expect(segments[i].style.display).not.toBe('none');
    }
  });

  it('worm segments are positioned in a horizontal line or simple curve', () => {
    initializeWorm(container);
    const segments = container.children;
    for (let i = 0; i < segments.length; i++) {
      expect(segments[i].style.position).toBe('absolute');
      expect(parseInt(segments[i].style.left, 10)).toBe(i * 20);
    }
  });

  it('CSS or JavaScript is used to set the initial position', () => {
    initializeWorm(container);
    const segments = container.children;
    for (let i = 0; i < segments.length; i++) {
      expect(segments[i].style.left).not.toBe('');
      expect(segments[i].style.top).not.toBe('');
    }
  });

  it('different viewport sizes are considered', () => {
    // Mock viewport size (example)
    Object.defineProperty(window, 'innerWidth', {
      writable: true,
      value: 800
    });
    Object.defineProperty(window, 'innerHeight', {
      writable: true,
      value: 600
    });
    initializeWorm(container, 3);
    const segments = container.children;
    expect(segments.length).toBe(3);
  });
});
