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

  def size(self):
    return self._size(self.root)

  def _size(self, node):
    if node is None:
      return 0
    return 1 + self._size(node.left) + self._size(node.right)


if __name__ == '__main__':
  bst = BinarySearchTree()
  numbers = input().split()
  for el in numbers:
    if el != '0':
      bst.insert(int(el))
    else:
      break
  print(bst.size())