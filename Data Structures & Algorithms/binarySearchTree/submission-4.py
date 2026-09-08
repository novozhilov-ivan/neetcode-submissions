class TreeNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)

        if not self.root:
            self.root = node
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = node
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.find_min(self.root)
        return curr.val if curr else -1

    def find_min(self, node) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)

    def remove_helper(self, curr, key) -> TreeNode:
        if curr is None:
            return None
        
        if key < curr.key:
            curr.left = self.remove_helper(curr.left, key)
        elif key > curr.key:
            curr.right = self.remove_helper(curr.right, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                min_node = self.find_min(curr.right)
                curr.key, curr.val = min_node.key, min_node.val
                curr.right = self.remove_helper(curr.right, min_node.key)
        
        return curr


    def getInorderKeys(self) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return res

