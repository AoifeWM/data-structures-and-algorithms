from data_structures.hashtable import Hashtable


def tree_intersection(tree_one, tree_two):
    ht = Hashtable()
    result = []
    for value in tree_one.pre_order():
        ht.set(value, 1)
    for value in tree_two.pre_order():
        if ht.contains(value) and value not in result:
            result.append(value)
    if len(result) > 0:
        return result
    return None
