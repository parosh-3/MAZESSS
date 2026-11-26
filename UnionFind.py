class UnionFind:
    def __init__(self, collec: int | list):
        if isinstance(collec, int):
            n = collec
        else:
            n = len(collec)

        self.parent = list(range(n))
        self.size = [1] * n

    def merge(self, index1: int, index2: int) -> None:
        if type(index1) != int:
            raise TypeError("index1 isn't an integer")
        if type(index2) != int:
            raise TypeError("index2 isn't an integer")
        if not 0 <= index1 < len(self.parent):
            raise IndexError("Index1 out of range")
        if not 0 <= index2 < len(self.parent):
            raise IndexError("Index2 out of range")

        actualIndex1 = self.find(index1)
        actualIndex2 = self.find(index2)

        if actualIndex1 == actualIndex2:
            return

        if self.size[actualIndex1] >= self.size[actualIndex2]:
            self.size[actualIndex1] += self.size[actualIndex2]
            self.parent[actualIndex2] = actualIndex1
            self.parent[index2] = actualIndex1
        else:
            self.size[actualIndex2] += self.size[actualIndex1]
            self.parent[actualIndex1] = actualIndex2
            self.parent[index1] = actualIndex2

    def find(self, node: int) -> int:
        if type(node) != int:
            raise TypeError("Node isn't an integer")
        if not 0 <= node < len(self.parent):
            raise IndexError("Node index out of range")

        reassign = []
        while self.parent[node] != node:
            reassign.append(node)
            node = self.parent[node]

        for index in reassign:
            self.parent[index] = node

        return node
            
