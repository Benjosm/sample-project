// crawling-worm-website/tests/gsap-inclusion.test.js
import { readFile } from 'node:fs/promises';
import { expect, it } from 'vitest';


it('should include GSAP library via CDN in index.html', async () => {
  const htmlContent = await readFile('crawling-worm-website/index.html', 'utf-8');
  expect(htmlContent).toContain('https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js');
});