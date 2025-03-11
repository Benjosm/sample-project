// tests/test_worm_position.js
const { updateWormPosition, worm, gridSize, gameBoardSize } = require('../script.js');
const chai = require('chai');
const assert = chai.assert;

describe('Worm Boundary Conditions', () => {
    it('should stay within bounds (left)', () => {
        const initialWorm = { x: 0, y: 0 };
        updateWormPosition(initialWorm, -1, 0, gameBoardSize, gridSize);
        assert.strictEqual(initialWorm.x, 0, 'X should stay at 0 (left boundary)');
    });
    it('should stay within bounds (right)', () => {
        const initialWorm = { x: 9, y: 0 };
        updateWormPosition(initialWorm, 1, 0, gameBoardSize, gridSize);
        assert.strictEqual(initialWorm.x, 9, 'X should stay at 9 (right boundary)');
    });
    it('should stay within bounds (top)', () => {
        const initialWorm = { x: 0, y: 0 };
        updateWormPosition(initialWorm, 0, -1, gameBoardSize, gridSize);
        assert.strictEqual(initialWorm.y, 0, 'Y should stay at 0 (top boundary)');
    });
    it('should stay within bounds (bottom)', () => {
        const initialWorm = { x: 0, y: 9 };
        updateWormPosition(initialWorm, 0, 1, gameBoardSize, gridSize);
        assert.strictEqual(initialWorm.y, 9, 'Y should stay at 9 (bottom boundary)');
    });
});