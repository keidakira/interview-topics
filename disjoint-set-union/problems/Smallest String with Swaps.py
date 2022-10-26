"""
Leetcode 1202. Smallest String With Swaps
Medium

URL: https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string s, and an array of pairs of indices in the string pairs
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string. You can
swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after
using the swaps.
"""
from typing import List

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

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        res = ["" for _ in range(n)]
        
        for x,y in pairs:
            uf.union(x, y)
        
        rootMap = {}
        for i in range(n):
            r = uf.find(i)
            if r in rootMap:
                rootMap[r].append(i)
            else:
                rootMap[r] = [i]
        
        for root in rootMap:
            string = []
            for i in rootMap[root]:
                string.append(s[i])
            
            string.sort()
            j = 0
            for i in rootMap[root]:
                res[i] = string[j]
                j += 1
        
        result = ""
        for string in res:
            result += string
        
        return result