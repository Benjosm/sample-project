// crawling-worm-website/tests/directory.test.js
import { describe, it, expect } from 'vitest';
import fs from 'fs';

describe('Project Directory', () => {
  it('should exist at the project root', () => {
    const directoryPath = 'crawling-worm-website';
    expect(fs.existsSync(directoryPath)).toBe(true);
  });
});