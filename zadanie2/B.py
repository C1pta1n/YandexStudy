import numpy as np

N, K = int(input()), int(input())
nums = []
for i in range(0,N):
    num = int(input())
    nums.append(num)
print(nums)
def countprefixsums(nums):
    prefixsumbyvalue = {0:1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] +=1
    return prefixsumbyvalue
def countsumranges(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges
cnt = countprefixsums(nums)
cnt1 = countsumranges(cnt)
print(cnt1)
print(cnt)