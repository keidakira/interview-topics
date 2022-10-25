"""
Disjoint Set Union (DSU) Quick Union

Union Find Algorithm

Time Complexity:
    O(n) for initialization
    O(n) for find
    O(n) for union

Space Complexity:
    O(n) for initialization
    O(1) for find
    O(1) for union
"""
class UnionFind:
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
    
    def union(self, p: int, q: int) -> None:
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return
        
        self.root[parent_p] = parent_q
    
    def find(self, p: int) -> int:
        while p != self.root[p]:
            p = self.root[p]
        return p
    
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)