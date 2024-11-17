def count_pairs(n, r, distances):
    answer = 0
    j = 0

    for i in range(n):
        while j < n and distances[j] - distances[i] <= r:
            j += 1
        answer += (n - j)

    return answer
n, r = map(int, input().split())
distances = list(map(int, input().split()))
result = count_pairs(n, r, distances)
print(result)