// tests/test_script.js

// Mock the document object for testing in a Node.js environment
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

// Read the index.html file
const fs = require('fs');
const path = require('path');
const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');


describe('script.js', () => {
  beforeEach(() => {
    // Set up the DOM before each test
    const dom = new JSDOM(html);
    global.document = dom.window.document;
    // Load the script
    require('../script.js');
  });

  afterEach(() => {
    // Clean up the DOM after each test
    delete global.document;
  });

  it('should get the worm container element', () => {
    const wormContainer = document.getElementById('worm-container');
    expect(wormContainer).toBeDefined();
  });
});