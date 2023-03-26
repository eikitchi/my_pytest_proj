from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([7, 8, 9], 0) != 8
    assert arrs.get([1, 1, 1, 1], 0, "nothing there") in [1, 2]
    assert arrs.get(["one", "two", "three"], 2, "this is not str") == "three"
    assert arrs.get(["one", 2, False, {1: "nothing"}], 1) == 2


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([5, 6, 7, 8], 1) == [6, 7, 8]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1], 0) == [1]