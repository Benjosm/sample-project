# tests/test_worm_direction.py
import pytest
from script import changeDirection  # Assuming 'changeDirection' is in script.js and we have a way to import and use it from python.  This is where the code needs to be updated.


@pytest.mark.parametrize(
    "current_direction, new_direction",
    [
        ("up", "down"),
        ("down", "up"),
        ("left", "right"),
        ("right", "left"),
    ],
)
def test_change_direction_opposite(current_direction, new_direction):
    # This is a placeholder and needs to be updated to work with the actual worm implementation.
    # If the function worked as intended, it would return the new direction.
    assert changeDirection(current_direction) == new_direction, f"Expected {new_direction} but got something else"

@pytest.mark.parametrize(
    "current_direction, new_direction",
    [
        ("up", "left"),
        ("down", "right"),
        ("left", "down"),
        ("right", "up"),
    ],
)
def test_change_direction_valid(current_direction, new_direction):
    # This is a placeholder and needs to be updated to work with the actual worm implementation.
    # If the function worked as intended, it would return the new direction.
    assert changeDirection(current_direction) == new_direction, f"Expected {new_direction} but got something else"


@pytest.mark.parametrize(
    "current_direction, new_direction",
    [
        ("up", "up"),
        ("down", "down"),
        ("left", "left"),
        ("right", "right"),
    ],
)
def test_change_direction_same(current_direction, new_direction):
    # This is a placeholder and needs to be updated to work with the actual worm implementation.
    # If the function worked as intended, it would return the new direction.
    assert changeDirection(current_direction) == new_direction, f"Expected {new_direction} but got something else"
