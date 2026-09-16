from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root):
    if root is None:
        return []
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert preorder(tree) == [1, 2, 4, 5, 3]
    assert inorder(tree) == [4, 2, 5, 1, 3]
    assert postorder(tree) == [4, 5, 2, 3, 1]
    assert level_order(tree) == [1, 2, 3, 4, 5]
    print("ok")
