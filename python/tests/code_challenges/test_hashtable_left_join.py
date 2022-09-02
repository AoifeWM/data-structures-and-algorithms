import pytest
from code_challenges.hashtable_left_join import left_join
from data_structures.hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["guide", "usher", "follow"],
    ]

    actual = left_join(synonyms, antonyms)

    # Note: changed to this condition (from "assert actual == expected") because hashtable ordering shouldn't matter
    for item in actual:
        assert item in expected
    for item in expected:
        assert item in actual


def test_left_join_none():
    l_hash = Hashtable()
    r_hash = Hashtable()
    l_hash.set("diligent", "employed")
    l_hash.set("fond", "enamored")
    l_hash.set("guide", "usher")
    r_hash.set("truth", "no cap")
    r_hash.set("delicious", "bussin")
    r_hash.set("factual", "fake news")

    expected = [

        ["diligent", "employed", None],
        ["guide", "usher", None],
        ["fond", "enamored", None]
    ]

    actual = left_join(l_hash, r_hash)

    for item in actual:
        assert item in expected
    for item in expected:
        assert item in actual


def test_left_join_failure():
    l_hash = Hashtable()
    r_hash = Hashtable()
    r_hash.set("diligent", "employed")
    r_hash.set("fond", "enamored")
    r_hash.set("guide", "usher")
    r_hash.set("truth", "no cap")
    r_hash.set("delicious", "bussin")
    r_hash.set("factual", "fake news")

    expected = []
    actual = left_join(l_hash, r_hash)

    assert actual == expected


