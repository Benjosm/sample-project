# tests/test_worm_position.py
import pytest
from script import updateWormPosition  # Assuming script.js is transpiled to script.py


def test_worm_exceeds_top_boundary():
    worm = {"x": 50, "y": 0}
    boundaries = {"width": 100, "height": 100}
    new_position = updateWormPosition(worm, "up", boundaries)
    assert new_position["y"] >= 0, "Worm should not go above the top boundary"


def test_worm_exceeds_bottom_boundary():
    worm = {"x": 50, "y": 99}
    boundaries = {"width": 100, "height": 100}
    new_position = updateWormPosition(worm, "down", boundaries)
    assert new_position["y"] <= 99, "Worm should not go below the bottom boundary"


def test_worm_exceeds_left_boundary():
    worm = {"x": 0, "y": 50}
    boundaries = {"width": 100, "height": 100}
    new_position = updateWormPosition(worm, "left", boundaries)
    assert new_position["x"] >= 0, "Worm should not go beyond the left boundary"


def test_worm_exceeds_right_boundary():
    worm = {"x": 99, "y": 50}
    boundaries = {"width": 100, "height": 100}
    new_position = updateWormPosition(worm, "right", boundaries)
    assert new_position["x"] <= 99, "Worm should not go beyond the right boundary"
