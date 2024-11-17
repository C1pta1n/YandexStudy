package main

import (
	"fmt"
	"math"
)

func vib(n,k int, cnt []int,){
	var rab []int
	var days int
	for i := 0; i < n; i++ {
		for j := i+1; j < n; j++ {
			if int(math.Abs(float64(cnt[i]-cnt[j]))) >= k{
				rab = append(rab, cnt[j])
			}
		}
		rab = nil
	}
}

func main () {
	var n, k, a int
	var cnt []int
	fmt.Scan(&n, &k)
	for i := 0; i < n; i++ {
		fmt.Scan(&a)
		cnt = append(cnt, a)
	}
}