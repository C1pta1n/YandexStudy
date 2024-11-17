A = []
n = int(input())
if (n >= 2 and n <=10):
    for i in range(n):
        num = int(input())
        if (num >= -100 and num <= 100):
            A.append(num)
max1 = -101
max2 = -101
cnt1 = 0
cnt2 = 0
for i in range(0,n):
    if A[i] >= max1:
        max1 = A[i]
        cnt1 = i
for i in range(n):
    if A[i] >= max2 and i != cnt1:
        max2 = A[i]
        cnt2 = i
print(max1 * max2)