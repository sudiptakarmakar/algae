from typing import List
from algae.clrs.common import TreeNode
from algae.clrs.common import ListNode


def create_tree(nodes: List[int]) -> TreeNode:
    """
    This is ideal for leetcode type binary tree visualizer
    """
    if not nodes:
        return None

    root = None
    if nodes[0] is not None:
        root = TreeNode(nodes[0])

    pipe = [root]
    node_index = 1
    node_count = len(nodes)
    while pipe:
        node = pipe.pop(0)
        if node_index < node_count and nodes[node_index] is not None:
            left = TreeNode(nodes[node_index])
            pipe.append(left)
            node.left = left
        node_index += 1
        if node_index < node_count and nodes[node_index] is not None:
            right = TreeNode(nodes[node_index])
            pipe.append(right)
            node.right = right
        node_index += 1
    return root


def create_list(nodes: List[int]) -> ListNode:
    if not nodes:
        return None

    head = ListNode(nodes[0])
    node = head
    for val in nodes[1:]:
        new_node = ListNode(val)
        new_node.prev = node
        node.next = new_node
        node = new_node
    return head
