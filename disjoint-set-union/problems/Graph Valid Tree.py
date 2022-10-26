"""
Leetcode 261. Graph Valid Tree
Medium

URL: https://leetcode.com/problems/graph-valid-tree/

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""
from typing import List

class UnionFind:
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
    
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
        
        self.count -= 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        
        for u,v in edges:
            if unionFind.find(u) == unionFind.find(v):
                return False
            
            unionFind.union(u, v)
        
        return unionFind.count == 1

if __name__ == "__main__":
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]
    solution = Solution()
    solution.validTree(n, edges)