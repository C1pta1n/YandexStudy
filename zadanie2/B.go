package main

import (
	"fmt"
	"math"
)

func main() {
	var N, K, sum, num int
	var cnt []int
	fmt.Scan(&N, &K)
	if N >= 1 && N <= 100000 && K >= 1 && K <= int(math.Pow(10, 9)) {
		for i := 0; i < N; i++ {
			fmt.Scan(&num)
			if num >= 1 {
				cnt = append(cnt, num)
			}
		}
		for i := 0; i < N; i++ {
			if cnt[i] == K {
				sum++
			}
		}
		for i := 0; i < N; i++ {
			num = cnt[i]
			for j := i + 1; j < N; j++ {
				if cnt[i]+cnt[j] == K && i != j {
					sum++
					break
				}
				if cnt[i]+cnt[j] != K {
					num += cnt[j]
				}
				if num == K {
					sum++
					break
				}
			}
		}
	}
	fmt.Print(sum)
}
