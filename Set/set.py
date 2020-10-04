class TreeNode:

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left_child = left
        self.right_child = right
        self._value = value
        self.parent = parent

    def tree_size(self, node):
        if node is None:
            return 0
        return 1 + self.tree_size(node.right_child) + self.tree_size(node.left_child)

    def value(self):
        return self._value

    def left(self):
        return self.left_child

    def right(self):
        return self.right_child

    """def delete(self):  # probably deletes only references
        del self.left_child
        del self.right_child
        del self.parent
        del self._value"""

    def delete(self):  # sets None to attributes
        self.left_child = None
        self.right_child = None
        self.parent = None
        self._value = None


class Set:

    def __init__(self):
        self.root = None

    def insert(self, *args):
        for i in args:
            if self.root is None:
                self.root = TreeNode(value=i)
            else:
                self._insert(node=TreeNode(value=i), parent_node=self.root)

    def _insert(self, node, parent_node):
        if node.value() < parent_node.value():  # goes left
            if parent_node.left() is None:
                parent_node.left_child = node
                node.parent = parent_node
            else:
                self._insert(node=node, parent_node=parent_node.left())

        elif node.value() > parent_node.value():  # goes right
            if parent_node.right() is None:
                parent_node.right_child = node
                node.parent = parent_node
            else:
                self._insert(node=node, parent_node=parent_node.right())

    def find(self, searched_value):
        if self.root is None:
            return False
        return self._find(searched_value, self.root)

    def _find(self, searched_value, current_node=None):  # default current_node should be self.root
        if searched_value == current_node.value():
            return True
        if searched_value < current_node.value() and current_node.left() is not None:  # goes left
            return self._find(searched_value=searched_value, current_node=current_node.left())
        elif searched_value > current_node.value() and current_node.right() is not None:  # goes left
            return self._find(searched_value=searched_value, current_node=current_node.right())
        return False

    def size(self):
        if self.root is None:
            return 0
        return self.root.tree_size(self.root)

    def tree_delete(self):
        if self.root is None:
            return None
        else:
            self._tree_delete(self.root.left())
            self._tree_delete(self.root.right())
        self.root = None

    def _tree_delete(self, node):
        if node.left() is not None:
            self._tree_delete(node=node.left())
        elif node.right() is not None:
            self._tree_delete(node=node.right())
        node.delete()


def main():
    set = Set()
    set.insert(10, 5, 12, 3, 7, 14, 6, 9)
    print(set.find(3))
    print(set.size())
    print('\ncalled delete')
    set.tree_delete()
    print(set.root)
    # print(set.root.value())
    # print(set.root.left_child)
    # print(set.size())
    # print(set.find(3))
    # print('', set.root.value(), '\n', set.root.left_child.value(), '\n', set.root.right_child.value())


if __name__ == "__main__":
    main()
