import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.parent.as_posix())

from bfs import Node, BFS


def init():
    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    zero.adjs = [one, two]
    one.adjs = [zero, three, four]
    two.adjs = [zero, four]
    three.adjs = [one, five]
    four.adjs = [one, two, five]
    five.adjs = [three, four]

    return [zero, one, two, three, four, five]

def test_bfs():
    nodes = init()

    bfs = BFS()
    bfs.search(nodes[0])

    assert bfs.get_dist(nodes[0]) == 0
    assert bfs.get_dist(nodes[1]) == 1
    assert bfs.get_dist(nodes[2]) == 1
    assert bfs.get_dist(nodes[3]) == 2
    assert bfs.get_dist(nodes[4]) == 2
    assert bfs.get_dist(nodes[5]) == 3
