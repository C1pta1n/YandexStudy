package main

import (
	"fmt"
	"math"
)

func main() {
	var N, K, sum, num int64
	var cnt []int64
	var pcnt []int64
	pcnt = append(pcnt, 0)
	fmt.Scan(&N, &K)
	if N >= 1 && N <= 100000 && K >= 1 && K <= int64(math.Pow(10, 9)) {
		for i := 0; int64(i) < N; i++ {
			fmt.Scan(&num)
			cnt = append(cnt, num)
		}
		for i := 1; int64(i) < N+1; i++ {
			sum += cnt[i-1]
			if sum == K {
				pcnt = append(pcnt, pcnt[i-1]+1)
				sum = 0
			}
			if sum > K {
				sum = cnt[i-1]
			}
			pcnt = append(pcnt, pcnt[i-1])
		}
	}
	fmt.Println(pcnt)
	fmt.Print(sum)
}
