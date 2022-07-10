from code_challenges.trees.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node

        current = self.root
        while current:
            # print("looping value: ", value, " current.value: ", current.value)
            if value < current.value:
                # print("left")
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break
            elif value > current.value:
                # print("right")
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break
            else:
                break

    def contains(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    break
        return False


if __name__ == "__main__":
    btree = BinarySearchTree()
    btree.add(5)
    btree.add(2)
    btree.add(6)
    print(btree.pre_order())
