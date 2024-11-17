def max_length_under_c(n, c, s):
    left = 0
    count_a = 0
    count_b = 0
    pairs = 0
    max_len = 0

    for right in range(n):
        if s[right] == 'a':
            count_a += 1
        elif s[right] == 'b':
            count_b += 1
            pairs += count_a 

        while pairs > c:
            if s[left] == 'a':
                count_a -= 1
            elif s[left] == 'b':
                count_b -= 1
                pairs -= count_a 
            left += 1

        max_len = max(max_len, right - left + 1)
    
    return max_len

n, c = map(int, input().split())
s = input().strip()
result = max_length_under_c(n, c, s)
print(result)