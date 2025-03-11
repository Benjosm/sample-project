# tests/test_worm_position.py
import pytest
from script import updateWormPosition  # Corrected import


@pytest.mark.parametrize(
    "direction, initial_x, initial_y, expected_x, expected_y",
    [
        ("up", 10, 10, 10, 9),
        ("down", 10, 10, 10, 11),
        ("left", 10, 10, 9, 10),
        ("right", 10, 10, 11, 10),
    ],
)
def test_update_worm_position(direction, initial_x, initial_y, expected_x, expected_y):
    worm = {"x": initial_x, "y": initial_y, "direction": direction}
    updateWormPosition(worm)
    assert worm["x"] == expected_x
    assert worm["y"] == expected_y