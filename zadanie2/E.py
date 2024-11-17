import heapq

def remove_medians(n, arr):
    max_heap = []
    min_heap = []
    
    result = []
    
    for number in arr:
        heapq.heappush(max_heap, -number)
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            to_min = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, to_min)
        if len(max_heap) > len(min_heap) + 1:
            to_min = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, to_min)
        elif len(min_heap) > len(max_heap):
            to_max = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -to_max)
        if len(max_heap) > len(min_heap):
            median = -max_heap[0]
        else:
            median = min(-max_heap[0], min_heap[0])
        if median == -max_heap[0]:
            heapq.heappop(max_heap)
        else:
            min_heap.remove(median)
            heapq.heapify(min_heap)

        result.append(median)

    return result

n = int(input().strip())
arr = list(map(int, input().strip().split()))
result = remove_medians(n, arr)
print(' '.join(map(str, result)))