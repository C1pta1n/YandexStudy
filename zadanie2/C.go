package main

import (
	"fmt"
)

func main() {
	var N, K, sum, num int
	var cnt, sumfin, cnt1 []int
	fmt.Scan(&N, &K)
	for i := 0; i < N; i++ {
		fmt.Scan(&num)
		cnt = append(cnt, num)
	}
	sumfin = append(sumfin, 0)
	for i := N - 1; i >= 0; i-- {
		for j := 0; j <= N-2; j++ {
			if cnt[i]-cnt[j] > K {
				sum++
			} else {
				break
			}
		}
	}
	fmt.Print(sum)
}
