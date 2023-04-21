from collections import deque
from typing import List, Optional

from .node import Node


class BFS:
    def __init__(self) -> None:
        self.path = []

    def search(self, start_node: Node, goal_node: Optional[Node] = None) -> None:
        queue = deque([start_node])
        start_node.seen = True
        start_node.dist = 0

        while queue:
            current_node = queue.popleft()

            self.path.append(current_node.idx)

            if current_node == goal_node:
                break

            for node in current_node.adjs:
                if not node.seen:
                    node.seen = True
                    node.dist = current_node.dist + 1
                    queue.append(node)

    def get_path(self) -> List:
        return [node for node in self.path]

    def get_dist(self, goal_node: Node) -> int:
        return goal_node.dist
