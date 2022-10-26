"""
Leetcode 1101. The Earliest Moment When Everyone Become Friends
Medium

URL: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        unionFind = UnionFind(n)

        for time, a, b in logs:
            unionFind.union(a, b)
            
            if unionFind.count == 1:
                return time
        
        return -1