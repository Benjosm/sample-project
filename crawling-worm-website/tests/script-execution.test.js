import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('Script Execution', () => {
  it('should execute the script without errors', async () => {
    // Mock console.log to prevent output during test
    const logSpy = vi.spyOn(console, 'log').mockImplementation(() => {});

    // Import the script. This will execute the script.
    await import('../crawling-worm-website/script.js');

    // Restore console.log
    logSpy.mockRestore();
  });
});