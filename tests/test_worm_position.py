# tests/test_worm_position.py
import pytest

# Assuming a simple worm class for testing
class Worm:
    def __init__(self, x, y, game_board_size=400, grid_size=20):
        self.x = x
        self.y = y
        self.game_board_size = game_board_size
        self.grid_size = grid_size

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # Boundary checks
        if self.x < 0: self.x = 0
        if self.x >= self.game_board_size: self.x = self.game_board_size - self.grid_size
        if self.y < 0: self.y = 0
        if self.y >= self.game_board_size: self.y = self.game_board_size - self.grid_size

    def get_position(self):
        return (self.x, self.y)


@pytest.fixture
def worm():
    return Worm(0, 0)

@pytest.fixture
def worm_at_edge():
    return Worm(380, 380)


def test_worm_initial_position(worm): # Renamed test_worm_initial_position
    assert worm.get_position() == (0, 0)


def test_worm_move_positive(worm): # Renamed test_worm_move_positive
    worm.move(20, 20)
    assert worm.get_position() == (20, 20)


def test_worm_move_negative(worm): # Renamed test_worm_move_negative
    worm.move(-20, -20)
    assert worm.get_position() == (0, 0) # Should stay at 0,0 because of boundary conditions.


def test_worm_move_mixed(worm): # Renamed test_worm_move_mixed
    worm.move(20, -20)
    assert worm.get_position() == (20, 0)


# This test should fail because of a bug. It is meant to test the position updating.
def test_worm_move_bug(worm): # Renamed test_worm_move_bug
    worm.move(40, 40)
    assert worm.get_position() == (40, 40) # This should be (40, 40), so the test should fail


def test_worm_move_boundary_right(worm_at_edge):
    worm_at_edge.move(20, 0)
    assert worm_at_edge.get_position() == (380, 380)


def test_worm_move_boundary_bottom(worm_at_edge):
    worm_at_edge.move(0, 20)
    assert worm_at_edge.get_position() == (380, 380)