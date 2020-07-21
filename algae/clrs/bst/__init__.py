from typing import List, Set
from algae.clrs.common import TreeNode


def insert_with_parent(root: TreeNode, node: TreeNode, link_parent=False) -> bool:
    if root is None:
        return ValueError("Root must not be None")
    if node.val < root.val:
        if root.left is None:
            root.left = node
            if link_parent:
                node.parent = root
            return True
        else:
            return insert_with_parent(root.left, node, link_parent)
    elif node.val > root.val:
        if root.right is None:
            root.right = node
            if link_parent:
                node.parent = root
            return True
        else:
            return insert_with_parent(root.right, node, link_parent)
    else:
        return False


def insert(root: TreeNode, node: TreeNode):
    if root is None:
        return ValueError("Root must not be None")
    if node.val < root.val:
        if root.left is not None:
            return insert(root.left, node)
        root.left = node
    elif node.val > root.val:
        if root.right is not None:
            return insert(root.right, node)
        root.right = node


def create(node_vals: List[int], link_parent=False) -> TreeNode:
    if not node_vals:
        return None
    root = TreeNode(val=node_vals[0])
    for val in node_vals[1:]:
        if link_parent:
            insert_with_parent(root, TreeNode(val), link_parent)
        else:
            insert(root, TreeNode(val))
    return root


def inorder(root: TreeNode) -> TreeNode:
    if root is None:
        return
    yield from inorder(root.left)
    yield root
    yield from inorder(root.right)


def preorder(root: TreeNode) -> TreeNode:
    if root is None:
        return
    yield root
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: TreeNode) -> TreeNode:
    if root is None:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root


def search(node: TreeNode, target: int):
    if target is None:
        return None
    if node is None or node.val == target:
        return node
    if target < node.val:
        return search(node.left, target)
    else:
        return search(node.right, target)
