import pytest
from insertion_sort import insertion_sort


def test_exists():
    assert insertion_sort


def test_insertion_sort():
    array = [7, 4, 2, 1, 9, 10, 3, 5, 8, 6]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = insertion_sort(array)
    assert actual == expected


@pytest.mark.xfail
def test_insertion_sort_xfail():
    array = ['string', 1, {"dictionaries": "cool"}]
    try:
        actual = insertion_sort(array)
    except TypeError:
        actual = None
    expected = [1, {"dictionaries": "cool"}, 'string']
    assert actual == expected

