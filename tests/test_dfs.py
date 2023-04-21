import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.parent.as_posix())

from node import Node
from dfs import DFS


def init():
    zero = Node(idx=0)
    one = Node(idx=1)
    two = Node(idx=2)
    three = Node(idx=3)
    four = Node(idx=4)
    five = Node(idx=5)
    six = Node(idx=6)
    seven = Node(idx=7)
    eight = Node(idx=8)
    nine = Node(idx=9)

    zero.adjs = [one, two]
    two.adjs = [four, five]
    three.adjs = [four]
    four.adjs = [zero]
    five.adjs = [six, seven]
    six.adjs = [seven, eight]
    seven.adjs = [eight]
    eight.adjs = [nine]

    return [zero, one, two, three, four, five, six, seven, eight, nine]

def test_1():
    dfs = DFS()
    nodes = init()
    dfs.search(nodes[0], nodes[1])
    path = dfs.get_path()

    assert path[-1] == 1

def test_2():
    dfs = DFS()
    nodes = init()
    dfs.search(nodes[5], nodes[9])
    path = dfs.get_path()

    assert path[-1] == 9

def test_3():
    dfs = DFS()
    nodes = init()
    dfs.search(nodes[4], nodes[1])
    path = dfs.get_path()

    assert path[-1] == 1
