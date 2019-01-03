# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

'''
需要一个哈希表map来存储原图中的节点和新图中的节点的一一映射。
map的作用在于替代bfs和dfs中的visit数组，一旦map中出现了映射关系，就说明已经复制完成，也就是已经访问过了。
'''

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @DFS
    def cloneGraph(self, node):
        if node == None:
            return node
        d = {}

        def dfs(n):
            if n in d:
                return d[n]
            ans = UndirectedGraphNode(n.label)
            d[n] = ans
            for i in n.neighbors:
                ans.neighbors.append(dfs(i))
            return ans

        return dfs(node)
    #bfs
    def cloneGraph2(self, node):
        if node == None:
            return node
        map = {}
        nodes = []
        #初始化结果
        newnode = UndirectedGraphNode(node.label)
        #map:m个node,每个node：label,neighbors
        map[node] = newnode
        nodes.append(node)

        while nodes:
            n = nodes.pop()
            for neighbor in n.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[n].neighbors.append(copy)
                    map[neighbor] = copy
                    nodes.append(neighbor)
                else:
                    map[n].neighbors.append(map[neighbor])
        return newnode