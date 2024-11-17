package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B, C, D, M, N int
	fmt.Scan(&A, &B, &C, &D)
	if A >= 0 && B >= 0 && C >= 0 && D >= 0 && float64(A) < math.Pow(10.0, 9.0) && float64(B) < math.Pow(10.0, 9.0) && float64(C) < math.Pow(10.0, 9.0) && float64(D) < math.Pow(10.0, 9.0) {
		if A == B {
			M = min(A, B)
		} else if (A == 0 || B == 0) && A != B {
			M = 1
		} else if A == 0 && B == 0 {
			M = 0
		} else {
			M = min(A, B) + 1
		}
		if (C == D) && A != B {
			N = min(C, D)
		} else if (C == 0 || D == 0) && C != D {
			N = 1
		} else if C == 0 && D == 0 {
			N = 0
		} else {
			N = min(C, D) + 1
		}
		fmt.Print(M, N)
	}
}
