# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneNode(node: 'Node', visit=None, graph=None) -> 'Node':
    if graph is None:
        graph = {}
    if visit is None:
        visit = set()
    copy = Node(node.val)
    visit.add(node)
    graph[node.val] = copy
    for neighbor in node.neighbors:
        if neighbor not in visit:
            copy.neighbors.append(cloneNode(neighbor, visit, graph))
        else:
            copy.neighbors.append(graph[neighbor.val])
    return copy


class Solution:
    def cloneGraph(self, node: 'Node'):
        if not node:
            return
        return cloneNode(node)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
