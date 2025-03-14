// crawling-worm-website/tests/index.test.js
import { readFile } from 'node:fs/promises';
import { expect, test } from 'vitest';

test('index.html contains UTF-8 meta tag', async () => {
  const html = await readFile('crawling-worm-website/index.html', 'utf8');
  expect(html).toContain('<meta charset="UTF-8">');
});