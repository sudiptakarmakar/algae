class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"TreeNode<{self.val}>"


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        nxt = f" - {self.next}" if self.next else ""
        return f"ListNode<{self.val}>"
