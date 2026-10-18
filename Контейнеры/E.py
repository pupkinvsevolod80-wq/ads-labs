class Deque:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push_front(self, item):
    self.items = [item] + self.items

  def push_back(self, item):
    self.items.append(item)

  def pop_front(self):
    if self.is_empty():
      return 'error'
    return self.items.pop(0)

  def pop_back(self):
    if self.is_empty():
      return 'error'
    return self.items.pop()

  def front(self):
    if self.is_empty():
      return 'error'
    return self.items[0]

  def back(self):
    if self.is_empty():
      return 'error'
    return self.items[-1]

  def size(self):
    return len(self.items)

  def clear(self):
    self.items.clear()


d = Deque()
while True:
  cmd = input().split()
  if not cmd:
    continue

  if cmd[0] == 'push_front':
    d.push_front(int(cmd[1]))
    print('ok')
  elif cmd[0] == 'push_back':
    d.push_back(int(cmd[1]))
    print('ok')
  elif cmd[0] == 'pop_front':
    print(d.pop_front())
  elif cmd[0] == 'pop_back':
    print(d.pop_back())
  elif cmd[0] == 'front':
    print(d.front())
  elif cmd[0] == 'back':
    print(d.back())
  elif cmd[0] == 'size':
    print(d.size())
  elif cmd[0] == 'clear':
    d.clear()
    print('ok')
  elif cmd[0] == 'exit':
    print('bye')
    break