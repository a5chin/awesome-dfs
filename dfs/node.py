class Node:
    def __init__(self, idx: int = 0) -> None:
        self.idx = idx
        self.adjs = []
        self.seen = False
        self.prev = None

    def __repr__(self) -> str:
        return f"Node(id: {self.idx}, adjs: {self.adjs}, seen: {self.seen})"
