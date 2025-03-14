// crawling-worm-website/tests/index.test.js
import { expect, test } from 'vitest';
import fs from 'fs/promises';
import path from 'path';

const filePath = path.resolve(__dirname, '../index.html');

test('index.html includes a <body> tag', async () => {
  try {
    const fileContent = await fs.readFile(filePath, 'utf-8');
    expect(fileContent).toContain('<body>');
  } catch (error) {
    console.error('Error reading file:', error);
    throw error;
  }
});
