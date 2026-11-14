import sys

class Node:

  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def search(self, key):
    return self._search(self.root, key)

  def _search(self, node, key):
    if node is None:
      return False
    if node.data == key:
      return True
    if key < node.data:
      return self._search(node.left, key)
    return self._search(node.right, key)

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, node, key):
    if node is None:
      return Node(key)
    if key < node.data:
      node.left = self._insert(node.left, key)
    elif key > node.data:
      node.right = self._insert(node.right, key)
    return node

  def _max_node(self, node):
    current = node
    while current.right is not None:
      current = current.right
    return current

  def delete(self, key):
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):
    if node is None:
      return node
    if key < node.data:
      node.left = self._delete(node.left, key)
    elif key > node.data:
      node.right = self._delete(node.right, key)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      max_node = self._max_node(node.left)
      node.data = max_node.data
      node.left = self._delete(node.left, max_node.data)
    return node

  def print_tree(self):
    self._print_tree(self.root, 0)

  def _print_tree(self, node, level):
    if node is None:
      return
    self._print_tree(node.left, level + 1)
    print('.' * level + str(node.data))
    self._print_tree(node.right, level + 1)


if __name__ == '__main__':
  bst = BinarySearchTree()
  for line in sys.stdin:
    parts = line.split()
    if not parts:
      continue
    cmd = parts[0]

    if cmd == 'ADD':
      n = int(parts[1])
      if bst.search(n):
        print('ALREADY')
      else:
        bst.insert(n)
        print('DONE')

    elif cmd == 'DELETE':
      n = int(parts[1])
      if bst.search(n):
        bst.delete(n)
        print('DONE')
      else:
        print('CANNOT')

    elif cmd == 'SEARCH':
      n = int(parts[1])
      if bst.search(n):
        print('YES')
      else:
        print('NO')

    elif cmd == 'PRINTTREE':
      bst.print_tree()
