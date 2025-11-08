self.index = 0  # to track the current element

        def build(bound):
            # if all elements processed OR value exceeds upper bound
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None
            
            root_val = preorder[self.index]
            self.index += 1
            
            # create node
            root = TreeNode(root_val)
            
            # all left values must be < root_val
            root.left = build(root_val)
            # all right values must be < bound and > root_val
            root.right = build(bound)
            
            return root

        return build(float('inf'))