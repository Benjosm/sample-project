import { describe, it, expect } from 'vitest';
import * as fs from 'node:fs';

describe('Project Directory', () => {
  it('should exist at the project root', () => {
    const directoryPath = 'crawling-worm-website';
    expect(fs.existsSync(directoryPath)).toBe(true);
  });
});