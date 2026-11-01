import heapq
import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    w = int(input_data[1])

    figures = []
    idx = 2
    for i in range(1, n + 1):
        a = int(input_data[idx])
        width = int(input_data[idx + 1])
        figures.append((a, a + width - 1, i))
        idx += 2

    input_data = None

    figures.sort(key=lambda x: x[0])

    h = []
    layers = []

    for l, r, fig_id in figures:
        if h and h[0][0] < l:
            prev_r, color = heapq.heappop(h)
        else:
            color = len(layers)
            layers.append([])
        layers[color].append(fig_id)
        heapq.heappush(h, (r, color))

    print(len(layers))
    res = []
    for layer in layers:
        res.extend(layer)
    print(' '.join(map(str, res)))