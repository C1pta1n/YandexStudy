package main

import (
	"fmt"
)

func main() {
	var x1, y1, x2, y2, x, y int
	fmt.Scan(&x1, &y1, &x2, &y2, &x, &y)
	if x < x1 {
		if y < y1 {
			fmt.Print("SW")
		}
		if y > y1 && y < y2 {
			fmt.Print("W")
		}
		if y > y2 {
			fmt.Print("NW")
		}
	}
	if x > x1 && x < x2 {
		if y < y1 {
			fmt.Print("S")
		}
		if y > y2 {
			fmt.Print("N")
		}
	}
	if x > x2 {
		if y < y1 {
			fmt.Print("SE")
		}
		if y > y1 && y < y2 {
			fmt.Print("E")
		}
		if y > y2 {
			fmt.Print("NE")
		}
	}
}
