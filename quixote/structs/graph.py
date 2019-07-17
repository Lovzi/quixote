
class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Graph(object):
    def __init__(self, n):
        self.map = [None for _ in range(n)]
        self.count = n

    def add_edge(self, a, b):
        if self.map[a] is None:
            self.map[a] = LinkNode(b)
        else:
            node = LinkNode(b)
            node.next = self.map[a]
            self.map[a] = node


