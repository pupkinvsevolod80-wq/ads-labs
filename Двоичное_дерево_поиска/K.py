import sys
class Node:
  __slots__ = ('data', 'left', 'right')

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
          break

  def next_element(self, key):
    curr_node = self.root
    ans = -1
    while curr_node is not None:
      data = curr_node.data
      if data == key:
        return data
      if key < data:
        ans = data
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    return ans


if __name__ == '__main__':
  tokens = sys.stdin.buffer.read().split()
  if tokens:
    n = int(tokens[0])
    bst = BinarySearchTree()
    out = []
    last_y = None
    idx = 1
    for _ in range(n):
      op = tokens[idx]
      x = int(tokens[idx + 1])
      idx += 2
      if op == b'+':
        if last_y is not None:
          x = (x + last_y) % 1000000000
        bst.insert(x)
        last_y = None
      else:
        y = bst.next_element(x)
        out.append(str(y))
        last_y = y
    if out:
      sys.stdout.write('\n'.join(out) + '\n')