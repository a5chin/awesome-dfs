class Node:
    def __init__(self, idx: int):
        self.idx = idx
        self.adjs = []
        self.seen = False
        self.dist = float('inf')

    def __repr__(self):
        return f"Node(id={self.idx}, adjs={self.adjs}, dist={self.dist})"
