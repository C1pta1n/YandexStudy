package main

import (
    "fmt"
)

func main() {
    var N, K int64
    fmt.Scan(&N, &K)
    sumCounts := make(map[int64]int64)
    sumCounts[0] = 1 
    var sum, currentSum int64

    for i := int64(0); i < N; i++ {
        var num int64
        fmt.Scan(&num)
        currentSum += num
        if count, exists := sumCounts[currentSum-K]; exists {
            sum += count
        }
        sumCounts[currentSum]++
		fmt.Println(sumCounts)
    }
    fmt.Print(sum)
}