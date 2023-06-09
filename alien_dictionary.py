# class Solution:
#     def findTopo(self, V, adj):
#         # Code here
#         indegree = [0] * V
#
#         for node in adj:
#             for neighbor in node:
#                 indegree[neighbor] += 1
#
#         queue = []
#         topo = []
#
#         for node, deg in enumerate(indegree):
#             if deg == 0:
#                 queue.append(node)
#
#         while queue:
#             node = queue.pop(0)
#
#             for neighbor in adj[node]:
#                 indegree[neighbor] -= 1
#
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)
#
#             topo.append(node)
#
#         return topo
#
#     def findOrder(self, alien_dict, N, K):
#         # code here
#         alien_list = [el for el in alien_dict]
#         # print(alien_list)
#         adj = [[] for _ in range(K)]
#         for i in range(N - 1):
#             str1 = alien_list[i]
#             str2 = alien_list[i + 1]
#
#             for j in range(min(len(str1), len(str2))):
#                 if str1[j] != str2[j]:
#                     adj[ord(str1[j]) - 97].append(ord(str2[j]) - 97)
#                     break
#
#         topo = self.findTopo(K, adj)
#
#         return ''.join([chr(el + 97) for el in topo])
#
#
# if __name__ == "__main__":
#     N = 5
#     K = 4
#     dict1 = ["baa", "abcd", "abca", "cab", "cad"]
#     ob = Solution()
#     print(ob.findOrder(dict1, N, K))


# User function Template for python3

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
        alien_list = [el for el in alien_dict]
        adj = [[] for _ in range(K)]
        for i in range(N - 1):
            str1 = alien_list[i]
            str2 = alien_list[i + 1]

            for j in range(min(len(str1), len(str2))):
                if str1[j] != str2[j]:
                    adj[ord(str1[j]) - 97].append(ord(str2[j]) - 97)
                    break

        topo = self.findTopo(K, adj)

        return ''.join([chr(el + 97) for el in topo])


# {
# Driver Code Starts
# Initial Template for Python 3

class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends
