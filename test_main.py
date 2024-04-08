from main import calculate_rectangle_area
from main import calculate_cuboid
from main import main



def test_calculate_rectangle_area():
    assert shape_coice(rectangle)
    assert calculate_rectangle_area(1,2) == 2

def test_calculate_cuboid():
    assert shape_coice(cuboid)
    assert calculate_cuboid(1,2,3) == 6



