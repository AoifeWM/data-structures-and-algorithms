import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_contains_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.contains("apple")


def test_get_something_that_isnt_there():
    hashtable = Hashtable()
    actual = hashtable.get('This key does not exist!')
    expected = None
    assert actual == expected


def test_key_list():
    hashtable = Hashtable()
    hashtable.set('aa', 1)
    hashtable.set('bb', 2)
    hashtable.set('cc', 3)
    hashtable.set('dd', 4)
    hashtable.set('ee', 5)
    actual = hashtable.keys()
    expected = ['aa', 'bb', 'cc', 'dd', 'ee']
    for key in expected:
        assert key in actual
    assert len(expected) == len(actual)

def test_collision():
    # The size of the hashtable is set to 1 to ensure collision
    hashtable = Hashtable(1)
    # Assert these keys will collide
    assert hashtable.hash('ned') == hashtable.hash('petunia') == hashtable.hash('bear')
    # Add data to hashtable
    hashtable.set('ned', 'puppy')
    hashtable.set('petunia', 'cat')
    hashtable.set('bear', 'wise old dog')
    # Test if .get() works
    actual_bear = hashtable.get('bear')
    expected_bear = 'wise old dog'
    assert actual_bear == expected_bear
    # Test if .keys() works
    actual_keys = hashtable.keys()
    expected_keys = ['ned', 'petunia', 'bear']
    for key in expected_keys:
        assert key in actual_keys
    assert len(expected_keys) == len(actual_keys)
    # Test if .contains() works
    assert hashtable.contains('petunia')


def test_hashes_are_in_range():
    hashtable = Hashtable()
    wordlist = ['a', 'and', 'if', 'or', 'when', 'maybe', 'this is a really long key to see if anything breaks! the '
                                                         'next key has uncommon characters.', 'Ͳ ͖Ŵ֍', ' ', 35, 2/7]
    for word in wordlist:
        assert hashtable.hash(word) < hashtable._size


# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#
#     actual = []
#
#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())
#
#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
#
#     assert actual == expected
