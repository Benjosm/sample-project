# tests/test_worm_position.py
import pytest
from script import updateWormPosition


@pytest.mark.parametrize("direction, expected_x, expected_y", [
    ("right", 11, 10),
    ("left", 9, 10),
    ("up", 10, 9),
    ("down", 10, 11)
])
def test_update_worm_position(direction, expected_x, expected_y):
    worm = {"x": 10, "y": 10}
    updateWormPosition(worm, direction)
    assert worm["x"] == expected_x
    assert worm["y"] == expected_y