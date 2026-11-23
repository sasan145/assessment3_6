from collections import deque
from dfs_binarytree import run_dfs_tree


# ============================================================
# DIAGRAM 1: BINARY TREE
# ============================================================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Level-order insert: place at first empty child slot."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def inorder(self, node="root"):
        node = self.root if node == "root" else node
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def preorder(self, node="root"):
        node = self.root if node == "root" else node
        if node is None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node="root"):
        node = self.root if node == "root" else node
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value]


# ============================================================
# DIAGRAM 2: BINARY SEARCH TREE
# ============================================================
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right
            else:
                return  # ignore duplicates

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.value:
                return True
            current = current.left if key < current.value else current.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:       # leaf or only right child
                return node.right
            if node.right is None:      # only left child
                return node.left
            successor = node.right      # two children: inorder successor
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def inorder(self, node="root"):
        node = self.root if node == "root" else node
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)


# ============================================================
# DIAGRAM 3: GRAPH
# ============================================================
class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            v = queue.popleft()
            order.append(v)
            for w in self.adj[v]:
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                order.append(v)
                for w in reversed(self.adj[v]):
                    if w not in visited:
                        stack.append(w)
        return order

    def display(self):
        for v, neighbors in self.adj.items():
            print(f"{v} -> {neighbors}")


# ============================================================
# MAIN
# ============================================================
def run_binary_tree():
    print("=== Diagram 1: Binary Tree ===")
    tree = BinaryTree()
    for v in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(v)
    print("Inorder:  ", tree.inorder())
    print("Preorder: ", tree.preorder())
    print("Postorder:", tree.postorder())


def run_bst():
    print("\n=== Diagram 2: Binary Search Tree ===")
    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)
    print("Inorder:", bst.inorder())
    print("Search 60:", bst.search(60))
    print("Search 99:", bst.search(99))
    bst.delete(50)
    print("After deleting 50:", bst.inorder())


def run_graph():
    print("\n=== Diagram 3: Graph ===")
    g = Graph()
    for u, v in [("S1", "A1"), ("S1", "S2"), ("A1", "A2"), ("S2", "A2"), ("A2", "N")]:
        g.add_edge(u, v)
    g.display()
    print("BFS from S1:", g.bfs("S1"))
    print("DFS from S1:", g.dfs("S1"))


def main():
    run_binary_tree()
    run_bst()
    run_graph()
    print()
    run_dfs_tree()


if __name__ == "__main__":
    main()