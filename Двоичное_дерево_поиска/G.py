class Node:

  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
    else:
      curr_node = self.root
      while True:
        if key < curr_node.data:
          if curr_node.left is None:
            curr_node.left = Node(key)
            break
          curr_node = curr_node.left
        elif key > curr_node.data:
          if curr_node.right is None:
            curr_node.right = Node(key)
            break
          curr_node = curr_node.right
        else:
          break

  def forks(self):
    return self._forks(self.root)

  def _forks(self, node):
    if node is None:
      return []
    if node.left is not None and node.right is not None:
      return self._forks(node.left) + [node.data] + self._forks(node.right)
    return self._forks(node.left) + self._forks(node.right)


if __name__ == '__main__':
  bst = BinarySearchTree()
  numbers = input().split()
  for el in numbers:
    if el != '0':
      bst.insert(int(el))
    else:
      break
  print(*bst.forks(), sep='\n')