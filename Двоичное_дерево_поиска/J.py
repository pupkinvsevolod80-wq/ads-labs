import sys
class Node:
  __slots__ = ('data', 'count', 'left', 'right')

  def __init__(self, key):
    self.data = key
    self.count = 1
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
        data = curr_node.data
        if key < data:
          if curr_node.left is None:
            curr_node.left = Node(key)
            break
          curr_node = curr_node.left
        elif key > data:
          if curr_node.right is None:
            curr_node.right = Node(key)
            break
          curr_node = curr_node.right
        else:
          curr_node.count += 1
          break

  def order_up(self):
    res = []
    self._order_up(self.root, res)
    if res:
      sys.stdout.write('\n'.join(res) + '\n')

  def _order_up(self, node, res):
    if node is None:
      return
    self._order_up(node.left, res)
    res.append(f'{node.data} {node.count}')
    self._order_up(node.right, res)


if __name__ == '__main__':
  bst = BinarySearchTree()
  for val in map(int, sys.stdin.buffer.read().split()):
    if val != 0:
      bst.insert(val)
    else:
      break
  bst.order_up()