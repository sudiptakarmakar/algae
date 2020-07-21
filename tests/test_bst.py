import pytest
from algae.clrs import bst


@pytest.mark.parametrize(
    "nodes, expected", [([1, 2, 3, 4, 5, 6, 7], 1), ([4, 2, 6, 1, 3, 5, 7], 4),],
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
    "nodes, expected",
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
def test_search(nodes, nonexistent):
    root = bst.create(nodes)
    assert bst.search(root, nonexistent) is None
