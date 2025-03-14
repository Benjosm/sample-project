// crawling-worm-website/tests/index.test.js
import { test, expect } from 'vitest';
import fs from 'fs/promises';
import path from 'path';

const getFileContent = async (filePath) => {
  try {
    const absolutePath = path.resolve(__dirname, '..', filePath);
    const content = await fs.readFile(absolutePath, 'utf-8');
    return content;
  } catch (error) {
    console.error(`Error reading file ${filePath}:`, error);
    throw error;
  }
};

test('website loads without errors', async () => {
  try {
    const html = await getFileContent('index.html');
    expect(html).toContain('<html');
  } catch (error) {
    expect(error).toBeFalsy(); // Ensure the test fails if there's an error
  }
});