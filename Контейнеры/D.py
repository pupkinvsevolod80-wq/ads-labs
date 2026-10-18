class Queue:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      return "error"
    return self.items.pop(0)

  def front(self):
    if self.is_empty():
      return "error"
    return self.items[0]

  def size(self):
    return len(self.items)

  def clear(self):
    self.items.clear()


q = Queue()

while True:
  cmd = input().split()
  if not cmd:
    continue

  if cmd[0] == "push":
    q.push(int(cmd[1]))
    print("ok")
  elif cmd[0] == "pop":
    print(q.pop())
  elif cmd[0] == "front":
    print(q.front())
  elif cmd[0] == "size":
    print(q.size())
  elif cmd[0] == "clear":
    q.clear()
    print("ok")
  elif cmd[0] == "exit":
    print("bye")
    break