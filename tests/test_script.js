// tests/test_script.js

// Mock the script.js module to avoid browser dependencies in the test environment
jest.mock('../script.js', () => ({
    // Mock any functions called in script.js that will be used in the test
    changeDirection: jest.fn(),
    // You might need to mock other functions as well depending on the script.js implementation
}));

const script = require('../script.js');

describe('Random direction changes', () => {
  beforeEach(() => {
    // Clear mock function calls before each test
    jest.clearAllMocks();
  });

  it('should call changeDirection function periodically', () => {
    // Arrange
    const intervalTime = 1000; // Example interval time, adjust as needed
    jest.useFakeTimers(); // Use fake timers
    
    // Act
    script.init(); // Assuming init sets up the timer. You might need to call a different function.

    // Fast-forward time to trigger the interval multiple times
    jest.advanceTimersByTime(intervalTime * 3);

    // Assert
    expect(script.changeDirection).toHaveBeenCalledTimes(3);

    // Clean up
    jest.useRealTimers();
  });

    it('changeDirection should change direction', () => {
        // Arrange
        script.changeDirection();
        // Assert
        expect(script.changeDirection).toHaveBeenCalled();
    });
});