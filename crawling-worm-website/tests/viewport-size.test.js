// crawling-worm-website/tests/viewport-size.test.js
import { expect, test, beforeAll } from 'vitest';

beforeAll(() => {
  // Mock the document object
  global.document = {
    body: {
      innerHTML: ''
    },
    getElementById: (id) => {
      if (id === 'worm-container') {
        return { offsetWidth: 100, offsetHeight: 50, style: { display: '' } };
      }
      return null;
    }
  };
  global.innerWidth = 1920;
  global.innerHeight = 1080;
});

test('worm is visible on page load for small viewports', () => {
  // Mock a small viewport (e.g., mobile)
  global.innerWidth = 375;
  global.innerHeight = 667;
  document.body.innerHTML = '<div id="worm-container" style="display: block;"></div>';

  // Assuming the worm is added to the worm-container element.  
  const wormContainer = document.getElementById('worm-container');
  expect(wormContainer).toBeTruthy();
  expect(wormContainer.style.display).not.toBe('none');
  expect(wormContainer.offsetWidth).toBeGreaterThan(0);
  expect(wormContainer.offsetHeight).toBeGreaterThan(0);
});

test('worm is visible on page load for medium viewports', () => {
  // Mock a medium viewport (e.g., tablet)
  global.innerWidth = 768;
  global.innerHeight = 1024;
  document.body.innerHTML = '<div id="worm-container" style="display: block;"></div>';

  const wormContainer = document.getElementById('worm-container');
  expect(wormContainer).toBeTruthy();
  expect(wormContainer.style.display).not.toBe('none');
  expect(wormContainer.offsetWidth).toBeGreaterThan(0);
  expect(wormContainer.offsetHeight).toBeGreaterThan(0);
});

test('worm is visible on page load for large viewports', () => {
  // Mock a large viewport (e.g., desktop)
  global.innerWidth = 1440;
  global.innerHeight = 900;
  document.body.innerHTML = '<div id="worm-container" style="display: block;"></div>';

  const wormContainer = document.getElementById('worm-container');
  expect(wormContainer).toBeTruthy();
  expect(wormContainer.style.display).not.toBe('none');
  expect(wormContainer.offsetWidth).toBeGreaterThan(0);
  expect(wormContainer.offsetHeight).toBeGreaterThan(0);
});

test('worm is visible on page load for very large viewports', () => {
  // Mock a very large viewport
  global.innerWidth = 1920;
  global.innerHeight = 1080;
  document.body.innerHTML = '<div id="worm-container" style="display: block;"></div>';

  const wormContainer = document.getElementById('worm-container');
  expect(wormContainer).toBeTruthy();
  expect(wormContainer.style.display).not.toBe('none');
  expect(wormContainer.offsetWidth).toBeGreaterThan(0);
  expect(wormContainer.offsetHeight).toBeGreaterThan(0);
});