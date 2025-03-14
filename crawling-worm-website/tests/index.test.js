// crawling-worm-website/tests/index.test.js
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { describe, it, expect } from 'vitest';

describe('index.html', () => {
  it('should contain a div with id \'worm-container\' inside the body', () => {
    const indexPath = resolve(__dirname, '../index.html');
    const html = readFileSync(indexPath, 'utf8');
    expect(html).toContain('<div id="worm-container">');
  });
});
