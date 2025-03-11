# tests/test_script.py
import pytest
from unittest.mock import patch

# Mock the window object and its dimensions
@pytest.fixture
def mock_window():
    class MockWindow:
        innerWidth = 800
        innerHeight = 600
    return MockWindow()

# Mock the document object and its body
@pytest.fixture
def mock_document():
    class MockDocument:
        body = type('obj', (object,), {"offsetWidth": 800, "offsetHeight": 600})()
    return MockDocument()


# Test to check if the direction changes when hitting the boundary
@pytest.mark.parametrize("initial_x, initial_y, direction_x, direction_y, expected_direction_x, expected_direction_y", [
    (10, 10, -1, 0, 1, 0),  # Hit left boundary
    (790, 10, 1, 0, -1, 0), # Hit right boundary
    (10, 10, 0, -1, 0, 1),  # Hit top boundary
    (10, 590, 0, 1, 0, -1),  # Hit bottom boundary
])
@patch("script.window", new_callable=lambda: mock_window())
@patch("script.document", new_callable=lambda: mock_document())
def test_boundary_collision(mock_document, mock_window, initial_x, initial_y, direction_x, direction_y, expected_direction_x, expected_direction_y):
    # This test assumes the existence of a "worm" object and its properties
    # and a function like "update_worm_position"
    # You will need to adapt the test to your code's structure

    # Mock the worm object
    class MockWorm:
        def __init__(self):
            self.head = {"x": initial_x, "y": initial_y}
            self.direction = {"x": direction_x, "y": direction_y}
            self.segments = [self.head]
            self.size = 10 # Assume each segment is of size 10.

    worm = MockWorm()

    # Import the script module after patching window and document
    import script
    # Mock the getRandomDirection function, to ensure our test can predict the output
    with patch("script.getRandomDirection") as mock_getRandomDirection:
      mock_getRandomDirection.return_value = {"x": expected_direction_x, "y": expected_direction_y}

      # Call the function that should update the worm's direction
      script.handleBoundaryCollision(worm)

    # Assert that the worm's direction has changed correctly.
    assert worm.direction["x"] == expected_direction_x
    assert worm.direction["y"] == expected_direction_y
