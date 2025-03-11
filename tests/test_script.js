// tests/test_script.js

// This is a test file for the script.js file.

const { add } = require('../script.js');

test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(4);
});