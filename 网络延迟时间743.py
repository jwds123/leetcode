'''
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。
'''
#求单源有向图的最长路径。
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        #长为N的列表
        '''
        Bellman-Ford算法，这个算法TLE。时间复杂度O(ne)， 空间复杂度O(n)。1108ms
        '''
        dist = [float('inf')] * N
        dist[K - 1] = 0#顶点，初始化--0>inf
        # 1.u=k时 dist[v]=min(dist[v], dist[k] + w)=w 2.u!=k : k-u-v之间 3.不联通：inf
        for i in range(N):
            for time in times:
                #print(time)
                u = time[0] - 1
                v = time[1] - 1
                w = time[2]
                #print(dist[v], dist[u] + w)
                dist[v] = min(dist[v], dist[u] + w)#动态规划

        return -1 if float('inf') in dist else max(dist)

    def networkDelayTime2(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        INF = 0x7FFFFFFF  # 无穷大标记
        edge = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

        dist = [INF] * (N + 1)
        visit = [False] * (N + 1)

        for time in times:  # 对图的邻接矩阵进行初始化
            edge[time[0]][time[1]] = time[2]
        dist[K] = 0  # 对距离数组进行初始化 dist[i]=dist(k,i)
        print(dist)

        for i in range(N):
            MIN = INF
            index = None
            for j in range(1, N + 1):
                if visit[j] == False and dist[j] < MIN:
                    print('j:',j)
                    print('before:',MIN)
                    MIN = dist[j]
                    print('after:',MIN)
                    index = j  # 挑选出一个可确定的节点,K可以到达的点，而不是距离无穷大的点。从节点K开始
            if index == None: return -1
            #print(index)
            visit[index] = True
            for j in range(1, N + 1): #从确定的点到其他点 dist(k,v)+dist(v,m)<dist(k,m)
                if visit[j] == False and MIN + edge[index][j] < dist[j]:
                    dist[j] = MIN + edge[index][j]  # 用该节点更新数组
        #print(dist)
        return max(dist[1:])


def main():
    sol = Solution()
    times=[[2,1,1],[2,3,3],[3,4,2],[1,3,1],[1,4,1]]
    print(sol.networkDelayTime2(times,4,3))



if __name__ == '__main__':
    main()