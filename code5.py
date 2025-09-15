 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

       # Step 1: BFS with coordinates
        q = deque([(root, 0, 0)])  # (node, row, col)
        nodes = []  # to store (col, row, value)

        while q:
            node, row, col = q.popleft()
            if node:
                nodes.append((col, row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))

        # Step 2: Sort nodes → by col, then row, then value
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))

        # Step 3: Group by col
        col_map = defaultdict(list)
        for col, row, val in nodes:
            col_map[col].append(val)

        # Step 4: Return grouped results in col order
        return [col_map[c] for c in sorted(col_map)]
