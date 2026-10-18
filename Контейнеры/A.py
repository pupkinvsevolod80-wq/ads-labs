class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      return "error"
    return self.items.pop()

  def back(self):
    if self.is_empty():
      return "error"
    return self.items[-1]

  def size(self):
    return len(self.items)

  def clear(self):
    self.items = []

stack = Stack()

while True:
  cmd = input().split()
  if not cmd:
    continue

  if cmd[0] == "push":
    stack.push(int(cmd[1]))
    print("ok")
  elif cmd[0] == "pop":
    print(stack.pop())
  elif cmd[0] == "back":
    print(stack.back())
  elif cmd[0] == "size":
    print(stack.size())
  elif cmd[0] == "clear":
    stack.clear()
    print("ok")
  elif cmd[0] == "exit":
    print("bye")
    break
