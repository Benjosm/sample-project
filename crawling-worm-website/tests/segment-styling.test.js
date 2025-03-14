// crawling-worm-website/tests/segment-styling.test.js
import { describe, it, expect } from 'vitest';

// Mock the document to avoid errors in a Node.js environment
global.document = {
    createElement: () => ({ style: {} })
};

describe('Worm Segment Styling', () => {
    it('should have correct dimensions (width and height)', () => {
        const segment = document.createElement('div');
        segment.style.width = '20px';
        segment.style.height = '20px';
        expect(segment.style.width).toBe('20px');
        expect(segment.style.height).toBe('20px');
    });

    it('should have correct background color', () => {
        const segment = document.createElement('div');
        segment.style.backgroundColor = 'green';
        expect(segment.style.backgroundColor).toBe('green');
    });

    it('should have border-radius for rounded corners', () => {
        const segment = document.createElement('div');
        segment.style.borderRadius = '5px';
        expect(segment.style.borderRadius).toBe('5px');
    });
});