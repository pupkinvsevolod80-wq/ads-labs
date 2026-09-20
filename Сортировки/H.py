from functools import cmp_to_key


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return self.x **2+ self.y **2


def cmp_points(a, b):
    return a.dist() - b.dist()


n = int(input())
points = []                      

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))  

points.sort(key=cmp_to_key(cmp_points))

for p in points:
    print(p.x, p.y)
