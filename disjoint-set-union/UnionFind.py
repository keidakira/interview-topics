"""
An optimized Union-Find data structure implementation.

Time Complexity:
    O(n) for initialization
    O(log(n)) or O(alpha(n)) for find
    O(log(n)) or O(alpha(n)) for union

Space Complexity:
    O(n) for initialization
    O(1) for find
    O(1) for union

References:
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/
"""
class UnionFind:
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return
        
        if self.rank[xroot] < self.rank[yroot]:
            self.root[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.root[yroot] = xroot
        else:
            self.root[yroot] = xroot
            self.rank[xroot] += 1