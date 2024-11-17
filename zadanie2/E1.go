package main

import (
    "fmt"
)

func main() {
    var n int
    fmt.Scan(&n)

    nums := make([]int, n)
    for i := 0; i < n; i++ {
        fmt.Scan(&nums[i])
    }

    results := make([]int, 0, n)
    left := []int{}
    right := []int{}

    for len(nums) > 0 {
        for _, num := range nums {
            if len(left) == 0 || num <= left[len(left)-1] {
                left = append(left, num)
            } else {
                right = append(right, num)
            }
            balance(&left, &right)
        }

        median := left[len(left)-1]
        results = append(results, median)
        left = left[:len(left)-1]

        balance(&left, &right)

        nums = []int{}
        for _, v := range left {
            nums = append(nums, v)
        }
        for _, v := range right {
            nums = append(nums, v)
        }
        balance(&left, &right)
    }

    for _, v := range results {
        fmt.Print(v, " ")
    }
}

func balance(left *[]int, right *[]int) {
    for len(*left) > len(*right)+1 {
        *right = append(*right, (*left)[len(*left)-1])
        *left = (*left)[:len(*left)-1]
    }
    for len(*right) > len(*left) {
        *left = append(*left, (*right)[0])
        *right = (*right)[1:]
    }
}