x1, y1, x2, y2, x, y = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
distx = []
for x1 in range(x2-x1):
    distx.append(int(x1))
disty = []
for y1 in range(y2-y1):
    disty.append(int(y1))
print(distx)
print(disty)