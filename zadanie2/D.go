package main

import (
	"fmt"
	"math"
	"sort"
)

func minDaysToCompleteTasks(n int, k int, tasks []int) int {
	sort.Ints(tasks)
	days := 0
	i := 0
	for i < n {
		days++
		currentTask := tasks[i]
		for i < n && int(math.Abs(float64(tasks[i]-currentTask))) <= k {
			i++
		}
	}

	return days
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	tasks := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&tasks[i])
	}
	result := minDaysToCompleteTasks(n, k, tasks)
	fmt.Println(result)
}
