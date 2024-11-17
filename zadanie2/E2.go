package main

import (
    "container/heap"
    "fmt"
)

type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *maxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

type minHeap []int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *minHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func main() {
    var n int
    fmt.Scan(&n)

    nums := make([]int, n)
    for i := 0; i < n; i++ {
        fmt.Scan(&nums[i])
    }

    maxH := &maxHeap{}
    minH := &minHeap{}
    heap.Init(maxH)
    heap.Init(minH)

    results := []int{}

    for _, num := range nums {
        heap.Push(maxH, num)
        if maxH.Len() > 0 && (minH.Len() == 0 || (*maxH)[0] > (*minH)[0]) {
            x := heap.Pop(maxH)
            heap.Push(minH, x)
        }
        if maxH.Len() < minH.Len() {
            x := heap.Pop(minH)
            heap.Push(maxH, x)
        }
    }
    for maxH.Len() > 0 {
        var median int

        if maxH.Len() > minH.Len() {
            median = (*maxH)[0]
        } else {
            median = (*maxH)[0]
        }
        results = append(results, median)
        heap.Pop(maxH)
    }
    for _, v := range results {
        fmt.Print(v, " ")
    }
}