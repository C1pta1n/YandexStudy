dist = []
n = int(input())
for i in range(n):
    dist.append(list(map(int,input.split())))
for via in range(n):
    for fr in range(n):
        for to in range(n):
            dist[fr][to] = min(matr[fr][to], matr[fr][via]+ matr[via][to])
for i in range(n):
    if dist[i][i] < 0:
        print(i)