// tests/test_worm_position.js
const { updateWormPosition, worm, gridSize, gameBoardSize } = require('../script.js');
const chai = require('chai');
const assert = chai.assert;

describe('Worm Boundary Conditions', () => {
    it('should stay within bounds (left)', () => {
        const initialWorm = { x: 0, y: 0 };
        updateWormPosition(initialWorm, -1, 0, gameBoardSize, gridSize);
        assert.strictEqual(worm.x, 0, 'X should stay at 0 (left boundary)');
    });
});