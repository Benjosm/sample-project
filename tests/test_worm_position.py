# tests/test_worm_position.py
import pytest

# Assuming worm.py exists and contains a Worm class or related functions
# You might need to adjust the import path based on your project structure.
# For example, if the worm class lives in a directory called 'game':
# from game.worm import Worm


@pytest.fixture
def worm():
    # Create a mock Worm object or however you instantiate it
    # This is just an example, adapt it to your code.
    class MockWorm:
        def __init__(self):
            self.x = 0
            self.y = 0

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

        def get_position(self):
            return (self.x, self.y)

    return MockWorm()



def test_worm_initial_position(worm):
    assert worm.get_position() == (0, 0), "Worm should start at (0, 0)"


def test_worm_move_positive(worm):
    worm.move(1, 1)
    assert worm.get_position() == (1, 1), "Worm should move correctly in positive direction"


def test_worm_move_negative(worm):
    worm.move(-1, -1)
    assert worm.get_position() == (-1, -1), "Worm should move correctly in negative direction"


def test_worm_move_mixed(worm):
    worm.move(1, -1)
    assert worm.get_position() == (1, -1), "Worm should move correctly in mixed direction"


def test_worm_move_large_values(worm):
    worm.move(100, -50)
    assert worm.get_position() == (100, -50), "Worm should move correctly with large values"
