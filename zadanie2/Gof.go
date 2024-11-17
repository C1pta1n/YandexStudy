package main

import (
	"fmt"
)

func maxLengthUnderC(n int, c int64, s string) int {
	left := 0
	countA := 0
	countB := 0
	pairs := int64(0)
	maxLen := 0

	for right := 0; right < n; right++ {
		if s[right] == 'a' {
			countA++
		} else if s[right] == 'b' {
			countB++
			pairs += int64(countA)
		}

		for pairs > c && left < n {
			if s[left] == 'a' {
				countA--
			} else if s[left] == 'b' {
				countB--
				pairs -= int64(countA)
			}
			left++
		}

		maxLen = max(maxLen, right-left+1)
	}

	return maxLen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n int
	var c int64
	fmt.Scan(&n, &c)
	var s string
	fmt.Scan(&s)

	result := maxLengthUnderC(n, c, s)
	fmt.Println(result)
}
