from code_challenges.linked_list.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=64, prime=811):
        self._size = size
        self._prime = prime
        self._table = [LinkedList() for _ in range(size)]

    def set(self, key, value):
        index = self.hash(key)
        current = self._table[index].head
        while current:
            if list(current.value.keys())[0] == key:
                current.value[key] = value
                return
            current = current.next
        self._table[index].insert({key: value})

    def get(self, key):
        current = self._table[self.hash(key)].head
        while current:
            if list(current.value.keys())[0] == key:
                return current.value[key]
            current = current.next
        return None

    def contains(self, key):
        current = self._table[self.hash(key)].head
        while current:
            if key in current.value:
                return True
            current = current.next
        return False

    def keys(self):
        keys = []
        for index in self._table:
            current = index.head
            while current:
                keys.append(list(current.value.keys())[0])
                current = current.next
        return keys

    def hash(self, key):
        hashed = 1
        for i, letter in enumerate(str(key)):
            hashed += ord(letter)+i
            hashed *= (ord(letter)+1)*i
        return (hashed * self._prime) % self._size
