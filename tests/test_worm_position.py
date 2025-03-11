# tests/test_worm_position.py
import pytest

# Assuming a simple worm class for testing
class Worm:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_position(self):
        return (self.x, self.y)


@pytest.fixture
def worm():
    return Worm(0, 0)


def test_worm_initial_position(worm):
    assert worm.get_position() == (0, 0)


def test_worm_move_positive(worm):
    worm.move(1, 1)
    assert worm.get_position() == (1, 1)


def test_worm_move_negative(worm):
    worm.move(-1, -1)
    assert worm.get_position() == (-1, -1)


def test_worm_move_mixed(worm):
    worm.move(1, -1)
    assert worm.get_position() == (1, -1)


# This test should fail because of a bug. It is meant to test the position updating.
def test_worm_move_bug(worm):
    worm.move(2, 2)
    assert worm.get_position() == (0, 0) # This should be (2, 2), so the test should fail