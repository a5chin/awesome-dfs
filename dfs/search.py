from typing import List

from node import Node


class DFS:
    def __init__(self) -> None:
        self.path = []

    def search(self, start_node: Node, goal_node: Node) -> None:
        stack = [start_node]

        while stack:
            current_node = stack.pop()

            if not current_node.seen:
                current_node.seen = True

                if current_node == goal_node:
                    self._find_path(current_node)
                    break

                for node in current_node.adjs:
                    if not node.seen:
                        node.prev = current_node
                        stack.append(node)

    def _find_path(self, goal_node: Node) -> None:
        self.path = []
        while goal_node:
            self.path.append(goal_node.idx)
            goal_node = goal_node.prev
        self.path.reverse()
