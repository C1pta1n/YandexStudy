package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var ansver string
	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()
	text := scanner.Text()
	nums := strings.Split(text, "")
	if text != "" {
		ansver = "no"
	} else {
		ansver = "yes"
	}
	for i := len(nums) - 1; i >= 0; i -= 2 {
		if nums[i] == string(')') && i-1 >= 0 {
			if nums[i-1] == string('(') {
				ansver = "yes"
			} else {
				ansver = "no"
				break
			}
		} else if nums[i] == string(']') && i-1 >= 0 {
			if nums[i-1] == string('[') {
				ansver = "yes"
			} else {
				ansver = "no"
				break
			}
		} else if nums[i] == string('}') && i-1 >= 0 {
			if nums[i-1] == string('{') {
				ansver = "yes"
			} else {
				ansver = "no"
				break
			}
		} else {
			ansver = "no"
			break
		}
	}
	fmt.Print(ansver)
}