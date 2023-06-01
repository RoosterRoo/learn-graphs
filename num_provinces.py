# User function Template for python3

class Solution:
    def __init__(self):
        self.dfs = []

    def getDFS(self, adjLs, v, vis):
        vis[v] = True

        for i in adjLs[v]:
            if not vis[i]:
                self.getDFS(adjLs, i, vis)

    def numProvinces(self, adj, V):
        # code here
        adjLs = [[] for _ in range(V)]
        vis = [False] * V
        for i in range(V):
            for j in range(V):
                if adj[i][j] and i != j:
                    adjLs[i].append(j)

        cnt = 0
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.getDFS(adjLs, i, vis)

        return cnt


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        V = int(input())
        adj = []

        for i in range(V):
            temp = list(map(int, input().split()))
            adj.append(temp)

        ob = Solution()
        print(ob.numProvinces(adj, V))
