"""
Assessment 3.6: DFS Methods in Tree
Name: SASAN

Depth-First Search (DFS) traversals for a general tree:
  - Preorder  (root, then children left to right)
  - Postorder (children left to right, then root)
  - Iterative DFS using an explicit stack
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child


def dfs_preorder(node, result=None):
    """Recursive DFS: visit the node first, then its children."""
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)
    for child in node.children:
        dfs_preorder(child, result)
    return result


def dfs_postorder(node, result=None):
    """Recursive DFS: visit the children first, then the node."""
    if result is None:
        result = []
    if node is None:
        return result
    for child in node.children:
        dfs_postorder(child, result)
    result.append(node.value)
    return result


def dfs_iterative(root):
    """Iterative DFS using a stack (preorder order)."""
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        # Push children in reverse so the leftmost child is processed first
        for child in reversed(node.children):
            stack.append(child)
    return result


def dfs_find(root, target):
    """Return the node containing target using DFS, or None if not found."""
    if root is None:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == target:
            return node
        stack.extend(reversed(node.children))
    return None


def build_SASAN_tree():
    """
    Builds this tree:

            A
          / | \\
         B  C  D
        / \\     \\
       E   F     G
    """
    a = TreeNode("A")
    b = a.add_child(TreeNode("B"))
    c = a.add_child(TreeNode("C"))
    d = a.add_child(TreeNode("D"))
    b.add_child(TreeNode("E"))
    b.add_child(TreeNode("F"))
    d.add_child(TreeNode("G"))
    return a


def run_dfs_tree():
    print("=== SASAN ===")
    root = build_SASAN_tree()
    print("Recursive preorder :", dfs_preorder(root))
    print("Recursive postorder:", dfs_postorder(root))
    print("Iterative DFS      :", dfs_iterative(root))
    target = "F"
    found = dfs_find(root, target)
    print(f"Search for {target!r}: {'found' if found else 'not found'}")


if __name__ == "__main__":
    run_dfs_tree()