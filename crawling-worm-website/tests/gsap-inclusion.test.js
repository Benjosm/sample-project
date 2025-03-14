import { describe, it, expect, beforeEach } from 'vitest';
import * as fs from 'node:fs';
import { JSDOM } from 'jsdom';

// Mock the global document and window
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="worm-container"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;
global.HTMLElement = dom.window.HTMLElement;

async function readFile(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

describe('GSAP inclusion', () => {
  it('should include GSAP library via CDN in index.html', async () => {
    const htmlContent = await readFile('crawling-worm-website/index.html');
    expect(htmlContent).toContain('https://cdnjs.cloudflare.com/ajax/libs/gsap');
  });
});