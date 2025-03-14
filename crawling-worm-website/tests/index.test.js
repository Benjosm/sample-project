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

describe('index.html', () => {
  it('should contain a div with id \'worm-container\' inside the body', async () => {
    const htmlContent = await readFile('crawling-worm-website/index.html');
    expect(htmlContent).toContain('<div id="worm-container">');
  });
});