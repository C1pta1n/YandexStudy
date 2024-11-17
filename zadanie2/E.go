package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, num int
	var cnt []int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&num)
		cnt = append(cnt, num)
	}
	var o []int
	for len(cnt) > 0 {
		sort.Ints(cnt)
		var median int
		n := len(cnt)
		if n%2 == 1 {
			median = cnt[n/2]
		} else {
			if cnt[n/2-1] < cnt[n/2] {
				median = cnt[n/2-1]
			} else {
				median = cnt[n/2]
			}
		}
		o = append(o, median)
		for i, v := range cnt {
			if v == median {
				cnt = append(cnt[:i], cnt[i+1:]...)
				break
			}
		}
	}
	for i := 0; i < n; i++ {
		fmt.Print(o[i], " ")
	}
}
