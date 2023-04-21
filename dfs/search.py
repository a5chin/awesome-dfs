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
                    self.path = [current_node.idx]

                    while current_node.parent:
                        self.path.append(current_node.parent.idx)
                        current_node = current_node.parent

                    self.path.reverse()
                    break

                for node in current_node.adjs:
                    if not node.seen:
                        node.parent = current_node
                        stack.append(node)

    def get_path(self) -> List:
        return [node for node in self.path]
