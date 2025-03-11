// tests/test_script.js

const { changeDirection, worm } = require('../script.js');

test('changeDirection should change the direction', () => {
  const initialDirection = 'up';
  worm.direction = initialDirection;
  changeDirection();
  expect(worm.direction).not.toBe(initialDirection);
});