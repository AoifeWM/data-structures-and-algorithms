from data_structures.hashtable import Hashtable


def left_join(left_hash, right_hash):
    joined = []

    for key in left_hash.keys():
        left_value = left_hash.get(key)
        right_value = None

        if right_hash.contains(key):
            right_value = right_hash.get(key)

        joined.append([key, left_value, right_value])

    return joined


print()
