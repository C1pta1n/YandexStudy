package main

import (
	"fmt"
)

func main() {
	var N, K, sum, num int64
	fmt.Scan(&N, &K)
	var cnt, pcnt []int64
	for i := 0; i < int(N); i++ {
		fmt.Scan(&num)
		cnt = append(cnt, num)
	}
	pcnt = append(pcnt, 0)
	for i := 1; int64(i) < N+1; i++ {
		pcnt = append(pcnt, pcnt[i-1]+cnt[i-1])
	}
	fmt.Println(pcnt)
	for i := N; i > 0; i-- {
		for j := i - 1; int(j) >= 0; j-- {
			if pcnt[i]-pcnt[j] == K && pcnt[i] > pcnt[j] {
				sum++
				break
			}
		}
	}
	fmt.Print(sum)
}
