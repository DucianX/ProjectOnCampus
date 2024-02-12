from board import Board
from stone import Stone
b = Board(300, 4, 75, 0)
s1 = Stone(75, 75, 35, "Black")
s2 = Stone(75, 75, 35, "Black")
cellDivider = 4
cellSize = 75


def test_is_occupied_initially_false():
    """Test that all board positions are initially unoccupied"""
    for x in range(cellDivider):
        for y in range(cellDivider):
            assert not (b.is_occupied(x * cellSize, y * cellSize))


def test_reject_place_occupied_place():
    """Test that the recorded location is marked as True"""
    b.record_location(75, 75)
    assert b.is_occupied(75, 75)
    assert not b.is_occupied(150, 150)


def test_get_nearest():
    """Test that the x, y is set to the nearest intersection point"""
    result1 = b.get_nearest_point(85, 85)
    expected1 = 75, 75
    result2 = b.get_nearest_point(200, 200)
    expected2 = 225, 225
    result3 = b.get_nearest_point(0, 0)
    expected3 = 225, 225
    assert result1 == expected1
    assert result2 == expected2
    assert not result3 == expected3
