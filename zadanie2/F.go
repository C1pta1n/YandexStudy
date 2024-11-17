package main

import (
	"fmt"
)

func main() {
	const mod = 1000000007
	var n int
	fmt.Scan(&n)
	a := make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	sumTriples := int64(0)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				sumTriples += a[i] * a[j] * a[k]
			}
		}
	}
	if sumTriples > 10000000 {
		fmt.Print(sumTriples % mod)
	} else {
		fmt.Println(sumTriples)
	}
}
