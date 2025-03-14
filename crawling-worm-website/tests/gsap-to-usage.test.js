// crawling-worm-website/tests/gsap-to-usage.test.js
import { describe, it, expect, vi } from 'vitest';
import * as gsap from 'gsap';

// Mock gsap to avoid actual animation during testing
vi.mock('gsap');


// Assuming script.js is the file that uses GSAP's to() method.
// The test below is a basic example and may need adjustment
// based on the actual implementation in script.js.

describe('GSAP `to()` method usage', () => {
  it('should use gsap.to() for animation', async () => {
    // Mock the document and any other dependencies if needed.
    document.body.innerHTML = '<div id="worm-container"></div>';
    const script = await import('../crawling-worm-website/script.js');
    
    // Find an element to animate
    const wormContainer = document.getElementById('worm-container');
    expect(wormContainer).toBeDefined();

    // Assert that gsap.to was called
    expect(gsap.to).toHaveBeenCalled();
  });
});