def modular_pow(a, b, mod):
    res = 1
    base = a % mod
    while b > 0:
        if b & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        b >>= 1
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))

    MOD = 1000000007

    total_sum = sum(a) % MOD

    sum_pairs = sum(a[i] * a[j] % MOD for i in range(n) for j in range(i + 1, n)) % MOD

    sum_triples = (total_sum * total_sum % MOD * total_sum % MOD - 
                   3 * total_sum % MOD * sum_pairs % MOD + 
                   2 * sum_pairs % MOD) % MOD

    if sum_triples < 0:
        sum_triples += MOD

    sum_triples = (sum_triples * modular_pow(6, MOD - 2, MOD)) % MOD

    print(sum_triples)
    
if __name__ == "__main__":
    main()