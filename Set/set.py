class TreeNode:

    def __init__(self, elem=None, left=None, right=None, parent=None):
        self.left_child = left
        self.right_child = right
        self.elem = elem
        self.parent = parent

    def tree_size(self):
        return 1 + self.tree_size(self.right) + self.tree_size(self.left)

    def elem(self):
        return self.elem()


class Set:
    elems = []

    def __init__(self):
        pass

    def values(self):
        return map(TreeNode.elem(),self.elems)

    def insert(self, *args):
        for i in args:
            node = TreeNode(elem=i)
            if node in self.values():
                continue
            for existing_elem in self.elems:
                
            self.elems.append(node)

    def find(self, node):
        if node in self.elems:
            return True
        else:
            return False

    def size(self):
        return len(self.elems)


def main():
    pass


if __name__ == "__main__":
    main()
