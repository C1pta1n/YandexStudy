package main

import (
	"fmt"
)

func main() {
	var x1, y1, x2, y2, x, y int
	fmt.Scan(&x1, &y1, &x2, &y2, &x, &y)
	var distx, disty []int
	minsh, mind := y2-y1, x2-x1
	if x > x1 && x < x2 {
		for i := x1; i < x2; i++ {
			distx = append(distx, i)
			if mind > (x - i) {
				mind = x - i
			}
		}
	} else {
		for i := x2; i < x2+(x2-x1); i++ {
			distx = append(distx, i)
			if mind > (x - i) {
				mind = x - i
			}
		}
	}
	if y > y1 && y < y2 {
		for i := y1; i < y2; i++ {
			disty = append(disty, i)
			if minsh > (y - i) {
				minsh = y - i
			}
		}
	} else {
		for i := y2; i < y2+(y2-y1); i++ {
			disty = append(disty, i)
			if minsh > (y - i) {
				minsh = y - i
			}
		}
	}
	if x > x1 && x < x2 {
		if uint(mind) == uint(minsh) {
			fmt.Print("WN")
		} else if uint(mind) > uint(minsh) {
			fmt.Print("N")
		} else {
			fmt.Print("W")
		}
	} else {
		if uint(mind) == uint(minsh) {
			fmt.Print("SE")
		} else if uint(mind) > uint(minsh) {
			fmt.Print("S")
		} else {
			fmt.Print("E")
		}
	}
}
