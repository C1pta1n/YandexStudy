package main

import (
    "fmt"
)

func main() {
    var n, r int
    fmt.Scan(&n, &r)
    d := make([]int, n)
    for i := 0; i < n; i++ {
        fmt.Scan(&d[i])
    }
    answer := 0
    j := 0
    for i := 0; i < n; i++ {
        for j < n && d[j] - d[i] <= r {
            j++
        }
        answer += (n - j)
    }
    fmt.Println(answer)
}