import abc


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, sequence=None):
        self._constructor(sequence=sequence)

    def _constructor(self, sequence=None):
        if sequence is None:
            self.root = None
        else:
            for single in sequence:
                pass

    def __str__(self):
        pass


class BinaryTree(Tree):
    def __init__(self):
        super().__init__()



class BinarySearchTree(BinaryTree):
    pass