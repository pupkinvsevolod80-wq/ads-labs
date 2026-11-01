class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        h = self.heap
        while i > 1:
            p = i // 2
            if h[i] > h[p]:
                h[i], h[p] = h[p], h[i]
                i = p
            else:
                break

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def shiftDown(self, i):
        h = self.heap
        size = self.size
        while 2 * i <= size:
            left = 2 * i
            right = left + 1
            j = left
            if right <= size and h[right] > h[left]:
                j = right
            if h[j] > h[i]:
                h[i], h[j] = h[j], h[i]
                i = j
            else:
                break

    def delMax(self):
        if self.size == 0:
            return None
        h = self.heap
        removed = h[1]
        last = h.pop()
        self.size -= 1
        if self.size > 0:
            h[1] = last
            self.shiftDown(1)
        return removed

    def clear(self):
        self.heap = [0]
        self.size = 0


def main():
    heap = MaxHeap()
    ans = []
    append = ans.append

    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
        
        c = line[0]
        if c == 'A':
            heap.insert(int(line[4:]))
        elif c == 'E':
            val = heap.delMax()
            if val is None:
                append('CANNOT')
            else:
                append(str(val))
        elif c == 'C':
            heap.clear()

    if ans:
        print('\n'.join(ans))


main()