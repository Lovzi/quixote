class Node(object):
    pass

class Tree(object):
    pass

class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(Tree):
    def __init__(self, lists=None):
        self.root = None
        if lists:
            for val in lists:
                node = BinaryTreeNode(val)
