// crawling-worm-website/tests/worm-segment-spacing.test.js
import { expect, test } from 'vitest';

// Assuming you have a way to render the worm segments and inspect their styles.
// This is a placeholder, adapt based on your actual implementation.

// Helper function to create a worm segment element (replace with your actual segment creation)
function createSegment(index, spacing) {
    const segment = document.createElement('div');
    segment.className = 'worm-segment';
    segment.style.left = `${index * (10 + spacing)}px`; // Assuming base size is 10px
    return segment;
}

test('worm segment spacing with different values', () => {
    // Test cases with different spacing values
    const testCases = [
        { spacing: 0, expectedLeftPositions: [0, 10, 20, 30, 40] },
        { spacing: 5, expectedLeftPositions: [0, 15, 30, 45, 60] },
        { spacing: 10, expectedLeftPositions: [0, 20, 40, 60, 80] },
    ];

    testCases.forEach(testCase => {
        const { spacing, expectedLeftPositions } = testCase;
        const segments = [];
        for (let i = 0; i < 5; i++) {
            segments.push(createSegment(i, spacing));
        }

        // Verify the spacing is correctly rendered
        segments.forEach((segment, index) => {
            const expectedLeft = `${expectedLeftPositions[index]}px`;
            expect(segment.style.left).toBe(expectedLeft);
        });
    });
});
