class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0] * V

        for node in adj:
            for neighbor in node:
                indegree[neighbor] += 1

        queue = []
        topo = []

        for node, deg in enumerate(indegree):
            if deg == 0:
                queue.append(node)

        while queue:
            node = queue.pop(0)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

            topo.append(node)

        return topo


import sys

sys.setrecursionlimit(10 ** 6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topoSort(N, adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
