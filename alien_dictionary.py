class Solution:
    def findTopo(self, V, adj):
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

    def findOrder(self, alien_dict, N, K):
        # code here
        adj = [[] for _ in range(K)]
        for i in range(N - 1):
            str1 = alien_dict[i]
            str2 = alien_dict[i + 1]

            for j in range(min(len(str1), len(str2))):
                if str1[j] != str2[j]:
                    adj[ord(str1[j]) - 97].append(ord(str2[j]) - 97)
                    break

        topo = self.findTopo(K, adj)

        return ''.join([chr(el + 97) for el in topo])


if __name__ == "__main__":
    N = 5
    K = 4
    dict1 = ["baa", "abcd", "abca", "cab", "cad"]
    ob = Solution()
    print(ob.findOrder(dict1, N, K))


