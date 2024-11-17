package main

import (
	"fmt"
)

func main() {
	var n, num, sum int
	var cnt []int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&num)
		cnt = append(cnt, num)
	}
	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			sum += cnt[j]
		}
		fmt.Print(sum, " ")
		sum = 0
	}
}
