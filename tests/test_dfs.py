import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.parent.as_posix())

from dfs import Node, DFS


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
three.adjs = [four]
five.adjs = [six, seven]
six.adjs = [seven, eight]
seven.adjs = [eight]
eight.adjs = [nine]

def test_1():
    dfs = DFS()
    dfs.search(zero, one)
    path = dfs.get_path()

    assert path[-1] == 1

def test_2():
    dfs = DFS()
    dfs.search(five, nine)
    path = dfs.get_path()

    assert path[-1] == 9

def test_3():
    dfs = DFS()
    dfs.search(one, three)
    path = dfs.get_path()

    assert path != 3
