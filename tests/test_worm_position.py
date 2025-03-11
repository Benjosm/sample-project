# tests/test_worm_position.py
import pytest
from script import updateWormPosition


@pytest.mark.parametrize(
    "direction, initial_x, initial_y, expected_x, expected_y",
    [
        ("right", 0, 0, 1, 0),
        ("left", 5, 5, 4, 5),
        ("up", 2, 2, 2, 1),
        ("down", 8, 8, 8, 9),
    ],
)
def test_update_worm_position(direction, initial_x, initial_y, expected_x, expected_y):
    worm = {"x": initial_x, "y": initial_y}
    updateWormPosition(worm, direction)
    assert worm["x"] == expected_x
    assert worm["y"] == expected_y
