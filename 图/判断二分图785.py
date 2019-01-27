import collections
import numpy as np
class Solution(object):
    def isBipartite(self, graph):
        """
        BFS 72ms 50%
        """
        #已经访问过的只能是两种颜色/两种集合，有边的分属两个集合
        visited = [0] * len(graph)# 0-not visited; 1-blue; 2-red;
        for i in range(len(graph)):
            #第i条边有没有遍历过,存入q中
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()#every point
                    for e in graph[v]:#v的所有邻接顶点
                        if visited[e] != 0:#已经访问过的，需要判断颜色，不能为相同颜色
                            if visited[e] == visited[v]:
                                return False
                        else:
                            #V与其邻接顶点的颜色和为3
                            visited[e] = 3 - visited[v]
                            q.append(e)
        return True

    def isBipartite2(self, graph):
        """
        DFS 50ms 100%
        """
        #已经访问过的只能是两种颜色/两种集合，有边的分属两个集合
        visited = [0] * len(graph)# 0-not visited; 1-blue; 2-red;
        for pos in range(len(graph)):
            if visited[pos]==0:
                if not self.dfs(graph,visited,pos,1):
                    return False
        return True


    def dfs(self, graph,visited,pos,c):
        """
        DFS
        """
        #已经访问过的只能是两种颜色/两种集合，有边的分属两个集合
        visited[pos]=c# 0-not visited; 1-blue; 2-red;
        for i in range(len(graph[pos])):
            if visited[graph[pos][i]]==c:
                return False
            #如果还没上色，当全部上色都不冲突就可以了
            if visited[graph[pos][i]]==0 and not self.dfs(graph,visited,graph[pos][i],3-c):
                return False
        return True



def main():
    sol=Solution()
    graph=[[1,3], [0,2], [1,3], [0,2]]
    # m = len(graph)
    # n = len(graph[0])
    # visited = np.zeros([m, n]).tolist()
    # print(visited)
    res=sol.isBipartite2(graph)
    print(res)

if __name__ == '__main__':
    main()