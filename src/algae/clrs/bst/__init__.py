from typing import Generator, List

from algae.clrs.common import TreeNode


class BinarySearchTree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def __repr__(self):
        return repr(f"BinarySearchTree<root={self.root.val if self.root else None}>")


# def insert(tree: BinarySearchTree, node: TreeNode, link_parent=False) -> bool:
#     if tree.root is None:
#         tree.root = node
#         node.parent = None
#         return True
#     root = tree.root
#     if node.val < root.val:
#         if root.left is not None:
#             return insert(root.left, node, link_parent)
#         root.left = node
#         if link_parent:
#             node.parent = root
#         return True
#     elif node.val > root.val:
#         if root.right is not None:
#             return insert(root.right, node, link_parent)
#         root.right = node
#         if link_parent:
#             node.parent = root
#         return True
#     else:
#         return False


# def transplant(tree: BinarySearchTree, target: TreeNode, replacement: TreeNode):
#     """Replace subtree under `target` by subtree under replacement inclusive"""
#     parent = target.parent
#     if parent is None:
#         tree.root = replacement
#     elif target == parent.left:
#         parent.left = replacement
#     else:
#         parent.right = replacement
#     if replacement is not None:
#         replacement.parent = target.parent


# def delete(tree: BinarySearchTree, target: TreeNode):
#     if target.left is None:
#         transplant(tree, target, target.right)
#     elif target.right is None:
#         transplant(tree, target, target.left)
#     else:
#         replacement = minimum(target.right)
#         if target == replacement.parent:
#             transplant(tree, replacement, replacement.right)
#             replacement.right = target.right
#             replacement.right.parent = replacement
#         transplant(tree, target, replacement)
#         replacement.left = target.left
#         replacement.left.parent = replacement


# def create(node_vals: List[int], link_parent=True) -> BinarySearchTree:
#     if not node_vals:
#         return BinarySearchTree(root=None)
#     root = TreeNode(val=node_vals[0])
#     tree = BinarySearchTree(root)
#     for val in node_vals[1:]:
#         insert(tree, TreeNode(val), link_parent)
#     return tree


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


def insert_iter(root: TreeNode, node: TreeNode):
    parent = None
    current = root
    while current is not None:
        parent = current
        if current.val > node.val:
            current = current.left
        elif current.val < node.val:
            current = current.right
        else:
            break
    node.parent = parent
    if parent is None:
        return node
    elif parent.val > node.val:
        parent.left = node
    elif parent.val < node.val:
        parent.right = node
    return root


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


def inorder(root: TreeNode) -> Generator[TreeNode, None, None]:
    if root is None:
        return
    yield from inorder(root.left)
    yield root
    yield from inorder(root.right)


def preorder(root: TreeNode) -> Generator[TreeNode, None, None]:
    if root is None:
        return
    yield root
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: TreeNode) -> Generator[TreeNode, None, None]:
    if root is None:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root


def search(node: TreeNode, target: int) -> TreeNode:
    if target is None:
        return None
    if node is None or node.val == target:
        return node
    if target < node.val:
        return search(node.left, target)
    else:
        return search(node.right, target)


def search_iter(node: TreeNode, target: int) -> TreeNode:
    if target is None:
        return None
    while node and node.val != target:
        if node.val > target:
            node = node.left
        else:
            node = node.right
    return node


def minimum(node: TreeNode) -> TreeNode:
    while node and node.left:
        node = node.left
    return node


def maximum(node: TreeNode) -> TreeNode:
    while node and node.right:
        node = node.right
    return node


def successor(node: TreeNode) -> TreeNode:
    if node and node.right:
        return minimum(node.right)
    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = parent.parent
    return parent


def predecessor(node: TreeNode) -> TreeNode:
    if node and node.left:
        return maximum(node.left)
    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = parent.parent
    return parent
