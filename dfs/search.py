from typing import List

from .node import Node


class DFS:
    def __init__(self) -> None:
        self.path = []

    def search(self, start_node: Node, goal_node: Node) -> None:
        stack = [start_node]

        while stack:
            current_node = stack.pop()

            if not current_node.seen:
                current_node.seen = True
                self.path.append(current_node)

                if current_node == goal_node:
                    break

                for node in current_node.adjs:
                    if not node.seen:
                        stack.append(node)

    def get_path(self) -> List:
        return [node.idx for node in self.path]
