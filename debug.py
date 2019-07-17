

from quixote.structs.graph import Graph


# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         graph = Graph(numCourses)
#         for t in prerequisites:
#             graph.add_edge(*t)
#         self.dfs(0, graph.map)
#
#     def dfs(self, v, graph):
#         if graph[v] is None:
#             return True
#         cur = graph[v]
#         while cur is not None:
#             if not self.dfs(cur.val, graph):
#                 return False
#             cur = cur.next
#         return True



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



class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = Graph(numCourses)
        for t in prerequisites:
            graph.add_edge(*t)
        vis = [False for i in range(numCourses)]
        for i in range(numCourses):
            if not self.dfs(i, graph.map, vis[:]):
                return False
        return True

    def dfs(self, v, graph, vis):
        if vis[v]:
            return False
        vis[v] = True
        if graph[v] is None:
            return True
        cur = graph[v]
        while cur is not None:
            if not self.dfs(cur.val, graph, vis):
                return False
            cur = cur.next
        return True

s = Solution()
print(s.canFinish(3, [[0,1],[0,2],[1,2]]))
