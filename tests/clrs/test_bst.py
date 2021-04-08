import pytest
from algae.clrs.common import TreeNode
from algae.clrs import bst


node_4 = None
node_6 = None
node_8 = None
node_9 = None
node_10 = None
node_11 = None
node_12 = None
node_14 = None
node_15 = None


def init_tree():
    """Test tree
             10
       6            14
    4     8      12     15
            9  11
    """
    global node_4, node_6, node_8, node_9, node_10, node_11, node_12, node_14
    global node_15, root

    node_9 = TreeNode(val=9)
    node_4 = TreeNode(val=4)
    node_8 = TreeNode(val=8, right=node_9)
    node_9.parent = node_8

    node_6 = TreeNode(val=6, left=node_4, right=node_8)
    node_4.parent = node_6
    node_8.parent = node_6

    node_11 = TreeNode(val=11)
    node_12 = TreeNode(val=12, left=node_11)
    node_11.parent = node_12
    node_15 = TreeNode(val=15)

    node_14 = TreeNode(val=14, left=node_12, right=node_15)
    node_12.parent = node_14
    node_15.parent = node_14

    node_10 = TreeNode(val=10, left=node_6, right=node_14)
    node_6.parent = node_10
    node_14.parent = node_10

    root = node_10


@pytest.mark.parametrize(
    "nodes, expected",
    [([1, 2, 3, 4, 5, 6, 7], 1), ([4, 2, 6, 1, 3, 5, 7], 4)],
)
def test_bst_create(nodes, expected):
    root = bst.create(nodes)
    assert root.val == expected


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
    ],
)
def test_inorder_traversal(nodes, expected):
    root = bst.create(nodes)
    index = 0
    for node in bst.inorder(root):
        assert node.val == expected[index]
        index += 1


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([4, 2, 6, 1, 3, 5, 7], [4, 2, 1, 3, 6, 5, 7]),
    ],
)
def test_preorder_traversal(nodes, expected):
    root = bst.create(nodes)
    index = 0
    for node in bst.preorder(root):
        assert node.val == expected[index]
        index += 1


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]),
        ([4, 2, 6, 1, 3, 5, 7], [1, 3, 2, 5, 7, 6, 4]),
    ],
)
def test_postorder_traversal(nodes, expected):
    root = bst.create(nodes)
    index = 0
    for node in bst.postorder(root):
        assert node.val == expected[index]
        index += 1


@pytest.mark.parametrize(
    "nodes, target",
    [
        ([4, 2, 6, 1, 3, 5, 7], 1),
        ([4, 2, 6, 1, 3, 5, 7], 2),
        ([4, 2, 6, 1, 3, 5, 7], 3),
        ([4, 2, 6, 1, 3, 5, 7], 4),
        ([4, 2, 6, 1, 3, 5, 7], 5),
        ([4, 2, 6, 1, 3, 5, 7], 6),
        ([4, 2, 6, 1, 3, 5, 7], 7),
    ],
)
def test_search(nodes, target):
    root = bst.create(nodes)
    result = bst.search(root, target)
    assert result.val == target


@pytest.mark.parametrize(
    "nodes, nonexistent",
    [
        ([4, 2, 6, 1, 3, 5, 7], 0),
        ([4, 2, 6, 1, 3, 5, 7], 10),
        ([4, 2, 6, 1, 3, 5, 7], None),
    ],
)
def test_search_fail(nodes, nonexistent):
    root = bst.create(nodes)
    assert bst.search(root, nonexistent) is None


@pytest.mark.parametrize(
    "nodes, target",
    [
        ([4, 2, 6, 1, 3, 5, 7], 1),
        ([4, 2, 6, 1, 3, 5, 7], 2),
        ([4, 2, 6, 1, 3, 5, 7], 3),
        ([4, 2, 6, 1, 3, 5, 7], 4),
        ([4, 2, 6, 1, 3, 5, 7], 5),
        ([4, 2, 6, 1, 3, 5, 7], 6),
        ([4, 2, 6, 1, 3, 5, 7], 7),
    ],
)
def test_search_iter(nodes, target):
    root = bst.create(nodes)
    result = bst.search_iter(root, target)
    assert result.val == target


@pytest.mark.parametrize(
    "nodes, nonexistent",
    [
        ([4, 2, 6, 1, 3, 5, 7], 0),
        ([4, 2, 6, 1, 3, 5, 7], 10),
        ([4, 2, 6, 1, 3, 5, 7], None),
    ],
)
def test_search_iter_fail(nodes, nonexistent):
    root = bst.create(nodes)
    assert bst.search_iter(root, nonexistent) is None


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 1),
        ([7, 6, 5, 4, 3, 2, 1], 1),
        ([4, 2, 6, 1, 3, 5, 7], 1),
    ],
)
def test_minimum(nodes, expected):
    root = bst.create(nodes)
    result = bst.minimum(root)
    assert result.val == expected


@pytest.mark.parametrize(
    "nodes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 7),
        ([7, 6, 5, 4, 3, 2, 1], 7),
        ([4, 2, 6, 1, 3, 5, 7], 7),
    ],
)
def test_maximum(nodes, expected):
    root = bst.create(nodes)
    result = bst.maximum(root)
    assert result.val == expected


def test_successor():
    init_tree()
    assert bst.successor(node_4) == node_6
    assert bst.successor(node_10) == node_11
    assert bst.successor(node_9) == node_10
    assert bst.successor(node_8) == node_9
    assert bst.successor(node_15) is None


def test_predecessor():
    init_tree()
    assert bst.predecessor(node_4) is None
    assert bst.predecessor(node_11) == node_10
    assert bst.predecessor(node_9) == node_8
    assert bst.predecessor(node_8) == node_6
    assert bst.predecessor(node_15) == node_14


def test_insert():
    pass


def test_insert_iter():
    pass
