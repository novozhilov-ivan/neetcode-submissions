"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        q = deque([node])
        old_to_new = {node: Node(node.val)}
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    q.append(neighbor)
                    old_to_new[neighbor] = Node(neighbor.val)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]
