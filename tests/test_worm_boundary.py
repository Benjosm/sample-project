# tests/test_worm_boundary.py
import pytest

# Assuming script.js contains the worm position logic and boundary definitions.
# We need to import the relevant functions or mock them if necessary.

# For example, if there's a function called updateWormPosition and variables for boundaries:
# from script import updateWormPosition, gameWidth, gameHeight

# Mock the necessary variables and functions to isolate the test
@pytest.fixture
def mock_game_environment(monkeypatch):
    monkeypatch.setattr("script.gameWidth", 500)
    monkeypatch.setattr("script.gameHeight", 500)
    # Optionally, mock updateWormPosition if it's needed
    # monkeypatch.setattr("script.updateWormPosition", lambda x, y: (x, y))



def test_worm_stays_within_boundaries(mock_game_environment):
    # Arrange
    start_x = 10
    start_y = 10
    # Act: Assume updateWormPosition updates the worm's position.  We need to define how this interacts with boundary conditions
    # For demonstration, we will assume this will move the worm outside the bounds
    # Ensure there is a function to update worm position or mock as necessary
    # updated_x, updated_y = script.updateWormPosition(600, 600) # Example of position exceeding boundaries
    updated_x = 600
    updated_y = 600 # Example of position exceeding boundaries

    # Assert
    assert updated_x <= script.gameWidth, f"Worm x-coordinate ({updated_x}) exceeded game width ({script.gameWidth})"
    assert updated_x >= 0, f"Worm x-coordinate ({updated_x}) went below 0"
    assert updated_y <= script.gameHeight, f"Worm y-coordinate ({updated_y}) exceeded game height ({script.gameHeight})"
    assert updated_y >= 0, f"Worm y-coordinate ({updated_y}) went below 0"
